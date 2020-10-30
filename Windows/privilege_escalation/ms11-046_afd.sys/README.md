# MS11-046 | Microsoft Windows (x86) - 'afd.sys' Local Privilege Escalation

1. Download [exploit code](https://www.exploit-db.com/exploits/40564)
2. Compile it

        i686-w64-mingw32-gcc MS11-046.c -o MS11-046.exe -lws2_32

3. Upload and execute the **MS11-046.exe** file on target system

## References

* https://www.exploit-db.com/exploits/40564
* https://www.youtube.com/watch?v=1eBi49J-XAE
* https://medium.com/@ranakhalil101/hack-the-box-devel-writeup-w-o-metasploit-88cc812794f1
* https://www.exploit-db.com/exploits/40564