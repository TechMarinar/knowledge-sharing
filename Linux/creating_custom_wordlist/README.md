# Creating Custom Wordlist

1. Use `grep` and `seclists` to prepare a custom wordlist

        grep '^co.*' /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt > fuzz.txt

2. Use [kwprocessor](https://github.com/hashcat/kwprocessor/releases/download/v1.00/kwprocessor-1.00.7z) to generate passwords based on keyboard sequences

        ./kwp basechars/full.base keymaps/en.keymap routes/2-to-16-max-3-direction-changes.route -s 1 -o wordlist.txt

3. [CeWL](https://tools.kali.org/password-attacks/cewl)

        cewl -d 2 -m 5 -w bludit_cewl.lst http://domain.com/

4. [Crunch](https://null-byte.wonderhowto.com/how-to/hack-like-pro-crack-passwords-part-4-creating-custom-wordlist-with-crunch-0156817/)

        crunch 8 8 -f /usr/share/rainbowcrack/charset.txt mixalpha-numeric -o /root/alphawordlist.lst

5. Try ready-made wordlists from [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials)
   
## References

* https://github.com/hashcat/kwprocessor
* https://tools.kali.org/password-attacks/cewl
* https://null-byte.wonderhowto.com/how-to/password-cracking/
* https://null-byte.wonderhowto.com/how-to/hack-like-pro-crack-passwords-part-4-creating-custom-wordlist-with-crunch-0156817/
* https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
* https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt