# Fuzzing

1. Guess the filename starting with prefix `db_`

        wfuzz -c -z file,fuzz.txt -t 20 --sc 200 http://example.com/db_FUZZ.txt

2. Test for SQL injection
   
        wfuzz -c -z file,/usr/share/wordlists/wfuzz/Injections/SQL.txt -d "username=admin&password=FUZZ" -u <TARGET_URL>

## References

* http://medium.com/@scottc130/how-to-use-wfuzz-to-fuzz-web-applications-8594c11d59d1
* https://certcube.com/wfuzz-cheat-sheet-the-power-of-brute-forcer/
* https://pentesterlab.com/exercises/from_sqli_to_shell_pg_edition/course
