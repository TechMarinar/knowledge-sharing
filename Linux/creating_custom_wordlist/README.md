# Creating Custom Wordlist

1. Use `grep` and `seclists` to prepare a custom wordlist

        $ grep '^co.*' /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt > fuzz.txt

2. Use [kwprocessor](https://github.com/hashcat/kwprocessor/releases/download/v1.00/kwprocessor-1.00.7z) to generate passwords based on keyboard sequences

        $ ./kwp basechars/full.base keymaps/en.keymap routes/2-to-16-max-3-direction-changes.route -s 1 -o wordlist.txt
   
## References

* https://github.com/hashcat/kwprocessor