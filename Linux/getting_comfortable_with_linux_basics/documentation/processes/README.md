# Processes

1. View **all** processes belonging to **current user**: `ps x`

        $ ps x
        PID TTY      STAT   TIME COMMAND
        719 ?        SLl   10:18 /opt/google/chrome/chrome
        734 ?        S      0:00 cat
        ...
        3686 pts/0    R+     0:00 ps x

    * **TTY** is short for “teletype,” and refers to the **controlling terminal** for the process. 
    * The presence of a “?” in the TTY column indicates no controlling terminal.
    * **STAT** is short for “state” and reveals the **current status** of the process

2. View **all** processes belonging to **every user**: `ps aux`

        $ ps aux | less

        USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
        root         1  0.0  0.0 169792 13828 ?        Ss   Oct05   1:14 /sbin/init splash

3. View processes **dynamically**

        top

4. **Kill** multiple processes matching a specified program or username

        killall [-u user] [-signal] name...

5. Ways to **shutdown** the system: `halt`, `poweroff`, `reboot`, `shutdown`

        reboot
        shutdown -h now
        shutdown -r now

6. View **process tree** specifiic to a user

        pstree root
