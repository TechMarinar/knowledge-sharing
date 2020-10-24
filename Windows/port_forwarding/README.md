# Port Forwarding

* Admin access is required to run following command in Windows

        netsh interface portproxy add v4tov4 listenaddress=10.10.10.4 listenport=8888 connectaddress=127.0.0.1 connectport=8888

* Non-admin users can use [plink](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to create SSH tunnel

        plink.exe -ssh -l <KaliUSERNAME> -pw <KaliPASSWORD> -N -R <KaliIP>:<KaliPORT>:127.0.0.1:8888 <KaliIP>   

## References

* https://www.onmsft.com/how-to/how-to-configure-port-forwarding-on-a-windows-10-pc