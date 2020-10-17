# Password Guessing/Cracking

1. **THC-Hydra**

        $ hydra -l username -P password_file.txt -s port -f ip_address request_method /path
        $ hydra -l john -P rockyou.txt -t 6 ssh://10.10.10.NNN

2. **HashCat**

        $ hashcat -a 0 -m 13100 ./hash.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/d3ad0ne.rule --force

3. **John the Ripper**

        $ sudo john --format=PuTTY --fork=4 key.hash -w=./wordlist.txt

## References

* http://tylerrockwell.github.io/defeating-basic-auth-with-hydra/
* https://tools.kali.org/password-attacks/hydra
* [Apache Tomcat Default Credentials - Dictionary Attack Payoad](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Default-Credentials/tomcat-betterdefaultpasslist.txt)
* https://www.youtube.com/watch?v=EfqJCKWtGiU
* https://www.hackingarticles.in/beginner-guide-john-the-ripper-part-1/
* https://www.youtube.com/watch?v=EfqJCKWtGiU
