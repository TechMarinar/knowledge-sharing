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
        export TERM=xterm
        press ctrl+z key combination 
        stty raw -echo
        fg

## References

* https://www.exploit-db.com/docs/english/44592-linux-restricted-shell-bypass-guide.pdf