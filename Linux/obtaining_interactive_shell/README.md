# Obtaining Interactive Shell

1. **Method 1**

        SHELL=/bin/bash script -q /dev/null
        Ctrl-Z
        stty raw -echo
        fg
        reset
        xterm

2. **Method 2**

        python3 -c "import pty;pty.spawn('/bin/bash')"

## References

* https://www.hackthebox.eu/