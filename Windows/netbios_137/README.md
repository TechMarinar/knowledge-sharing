# NetBIOS: Port 137, 138, 139

* Collect NetBIOS information

        sudo nbtscan -r 10.10.10.4
        sudo nbtscan -r 10.10.10.4 -v
        sudo nbtscan -r 10.10.10.4 -vh
        sudo nmap -v -sU -p 137 --script nbstat.nse 10.10.10.4

* Check if there are known vulnerabilities

        nmap --script vuln -p 137,139,445 10.10.10.4

## References

* https://10dsecurity.com/saying-goodbye-netbios/
* https://null-byte.wonderhowto.com/how-to/enumerate-netbios-shares-with-nbtscan-nmap-scripting-engine-0193957/