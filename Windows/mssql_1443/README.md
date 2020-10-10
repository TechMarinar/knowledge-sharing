# MSSQL: Port 1443

1. A quick nmap scan

        nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 <IP>

2. Connect to MSSQL server using [Impacket](../../Network/Network/impacket_tools/README.md)'s `mssqlclient.py` tool (when database credentials are known)

        $ ./examples/mssqlclient.py username@10.12.13.4

3. Once connected, try following commands

        SQL> select suser_name()
        SQL> select name,sysadmin from syslogins
        SQL> select srvname,isremote from sysservers

    Identify any linked server

4. Execute queries on a **linked server**, if any

        SQL> exec('select current_user') at [LinkedServer\ServerName];
        SQL> exec('select name,sysadmin from syslogins') at [LinkedServer\ServerName];
        SQL> exec('select srvname,isremote from sysservers') at [LinkedServer\ServerName];
        SQL> exec('exec(''select suser_name()'') at [NestedLinkedServer\NestedServerName]') at [LinkedServer\ServerName]

## Resources

* https://book.hacktricks.xyz/pentesting/pentesting-mssql-microsoft-sql-server
* https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xp-cmdshell-transact-sql?view=sql-server-ver15