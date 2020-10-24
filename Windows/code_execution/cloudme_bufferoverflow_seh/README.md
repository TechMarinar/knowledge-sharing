# CloudMe Sync 1.11.2 Buffer Overflow + SEH

CloudMe Sync is a synchronization application which syncs local storage with the cloud storage. It listens on port 8888 by default.

1. Check if the service is running on port 8888

        C:\> sc queryex type=service state=all | find /i "CloudMe"
        C:\> netstat -ano | find "8888"

2. Create remote SSH tunnel between Windows and Kali Linux in order to access the restricted service remotely
   1. Start SSH service in Kali

            sudo service ssh start
            sudo ss -antlp | grep sshd

   2. Check architecture of Windows machine, and download the right version of [plink.exe](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

            wmic os get osarchitecture

   3. Check firewall rules

            netsh firewall show config

   4. Create SSH tunnel by initiating tunneling from the Windows machine

            plink.exe -ssh -l <KaliUSERNAME> -pw <KaliPASSWORD> -N -R <KaliIP>:<KaliPORT>:127.0.0.1:8888 <KaliIP>

## References

* https://bufferoverflows.net/practical-exploitation-part-1-cloudme-sync-1-11-2-bufferoverflow-seh/
* https://medium.com/@informationsecurity/remote-ssh-tunneling-with-plink-exe-7831072b3d7d
* https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
* https://www.fireeye.com/blog/threat-research/2019/01/bypassing-network-restrictions-through-rdp-tunneling.html