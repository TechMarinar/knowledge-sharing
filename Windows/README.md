# Attacking a Windows Box

This repository contains hands-on training content on how to attack a Windows box.

1. [Windows Server Administration Basics](windows_server_administration_basics/README.md)
2. [MSSQL: Port 1433](mssql_1443/README.md)
3. [LDAP: Port 389](ldap_389/README.md)
4. [Kerberos Pre-authentication: Port 88](kerberos_preauthentication/README.md)
5. [WinRM: Port 5985,5986](winrm_5985/README.md)
6. [IIS Short File Name Disclosure](iis/README.md)
7. [DS_Walk: If .DS_Store file is public](ds_walk/README.md)
8. [SSH: Port 22](ssh_22/README.md)
9. Code Execution
   * [SQL Injection](https://resources.infosecinstitute.com/anatomy-of-an-attack-gaining-reverse-shell-from-sql-injection/)
   * [Microsoft IIS WebDAV Write Access Code Execution](https://www.rapid7.com/db/modules/exploit/windows/iis/iis_webdav_upload_asp)
10. Reverse Shell
    * [Powercat](reverse_shell/reverse_shell_powercat/README.md)
    * [PowerShell Reverse Shell](reverse_shell/powershell_reverse_shell/README.md)
    * [windows-php-reverse-shell](https://raw.githubusercontent.com/Dhayalanb/windows-php-reverse-shell/master/Reverse%20Shell.php)
11. [Post Exploitation](windows_post_exploitation/README.md)
    * [SharpHound: Data Collector](windows_post_exploitation/sharphound/README.md)
    * [CrackMapExecWin: Subnet Scanner](windows_post_exploitation/crackmapexecwin/README.md)
    * [Getting Indirect Shell in Restricted Environment](windows_post_exploitation/indirect_shell/README.md)
    * [SMBServer: File Transfer](windows_post_exploitation/file_transfer_smbserver/README.md)
    * [PowerShell: File Transfer](windows_post_exploitation/file_transfer_powershell/README.md)
    * [ROBOCOPY: Reverse File Transfer](windows_post_exploitation/reverse_file_transfer/README.md)
    * [Finding Readable/Writable Files & Directories](windows_post_exploitation/readable_writable_file_directory_enumeration/README.md)
    * [Active Directory Enumeration](windows_post_exploitation/active_directory_enumeration/README.md)
    * [Attacking Kerberos](windows_post_exploitation/attacking_kerberos/README.md)

12. [MSFvenom: Generating Attack Payload](generating_attack_payload/README.md)
13. Privilege Escalation
    * [AlwaysInstallElevated](privilege_escalation/alwaysinstallelevated/README.md)
    * [GetChangesAll](privilege_escalation/getchangesall/README.md)
    * [CVE-2019-1388: GUI Interaction Required](https://github.com/jas502n/CVE-2019-1388)
    * [Juicy Potato: From Service Accounts to SYSTEM](privilege_escalation/juicy_potato/README.md)
      * https://book.hacktricks.xyz/windows/windows-local-privilege-escalation/juicypotato
      * [Rotten Potato: Windows Server 2016 OS](https://foxglovesecurity.com/2016/09/26/rotten-potato-privilege-escalation-from-service-accounts-to-system/)
      * https://hunter2.gitbook.io/darthsidious/privilege-escalation/juicy-potato
