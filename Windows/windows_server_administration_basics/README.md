# Windows Server Administration Basics

**Active Directory** is a tool used to administrate domain users' accounts and computers. It can be used to:

* Create new user accounts
* Reset user passwords
* Manage computer accounts
* Mangae file shares
* Manage shared printers
* etc. 

**Common server roles** include following:
  * Active Directory Domain Services
  * DNS (Domain Name System)
  * DHCP (Dynamic Host Configuration Protocol)
  * WSUS (Windows Server Update Services)
  * WDS (Windows Deployment Services)
  * IIS (Internet Information Services)

## Points to Note

1. Regular user accounts *cannot* log into **Domain Controllers**.
2. To install a package with elevated (system) privileges, **AlwaysInstallElevated** value should be set to "**1**" under both of the following registry keys:

        HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
        HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer

    This setting allows low privileged users to create a Windows Installer package (MSI) and execute commands as SYSTEM.

## Learning Resources

* [Active Directory Tutorial for Beginners](https://www.youtube.com/watch?v=nKcrVtvZvpk)
* https://serveracademy.s3.amazonaws.com/Intro+to+IT.pdf
* https://book.hacktricks.xyz/windows/windows-local-privilege-escalation/integrity-levels
* https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated