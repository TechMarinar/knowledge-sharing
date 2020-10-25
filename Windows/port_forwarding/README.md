# Port Forwarding

* Admin access is required to run following command in Windows

        netsh interface portproxy add v4tov4 listenaddress=10.10.10.4 listenport=8888 connectaddress=127.0.0.1 connectport=8888

## PLINK

1. Enabled SSH on Kali

        $ sudo ss -antlp | grep sshd
        $ sudo service ssh start


2. Local port forward `TCP 22` on Kali to a different port, say `TCP 2222`

        sudo ssh -f -N -L 0.0.0.0:2222:127.0.0.1:22 root@localhost

3. Non-admin users can use [plink](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to create SSH tunnel

        plink.exe -ssh -l <KaliUSERNAME> -pw <KaliPASSWORD> -N -R <KaliIP>:<KaliPORT>:127.0.0.1:8888 <KaliIP>   

## References

* https://www.onmsft.com/how-to/how-to-configure-port-forwarding-on-a-windows-10-pc
* https://medium.com/@informationsecurity/remote-ssh-tunneling-with-plink-exe-7831072b3d7d
* https://www.reddit.com/r/hackthebox/comments/iyude1/outbound_connection_ssh_port_and_configuration/