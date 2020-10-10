# Creating Custom Wordlist

1. Use `grep` and `seclists` to prepare a custom wordlist

        $ grep '^co.*' /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt > fuzz.txt
