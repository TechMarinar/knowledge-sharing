# Port Forwarding

* Admin access is required to run following command

        netsh interface portproxy add v4tov4 listenaddress=10.10.10.4 listenport=8888 connectaddress=127.0.0.1 connectport=8888

## References

* https://www.onmsft.com/how-to/how-to-configure-port-forwarding-on-a-windows-10-pc