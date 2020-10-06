# Expansion

1. `*` (**Pathname expansion**): Find the difference between the outputs of following commands:

        echo this is a test
        echo *
        echo D*
        echo *s
        echo [[:upper:]]*
        echo /usr/*/share

    The shell expands `*` into names of files in current working directory.

2. `~` (**Tilde expansion**): Find home directory of a named user:

        echo ~foo

3. Arithmetic expansion `$((expression))`:

        echo $(($((5**2)) * 3))
        echo $(((5**2) * 3))
        echo with $((5%2)) left over.

4. `{}` (**Brace expansion**): Create multiple text strings from a pattern containing braces

        $ echo Front-{A,B,C}-Back
        Front-A-Back Front-B-Back Front-C-Back

        $ echo Number_{1..5}
        Number_1 Number_2 Number_3 Number_4 Number_5

        $ echo Number_{5..01}
        Number_05 Number_04 Number_03 Number_02 Number_01

        $ echo a{A{01..3},B{Z..X}}b
        aA01b aA02b aA03b aBZb aBYb aBXb

        $ mkdir {2020..2015}-{01..12}
        $ rm -r {2020..2015}-{01..12}

5. **Parameter expansion**

        echo $USER
        printenv | less

6. **Command substitution**

        ls -l $(which cp)
        ls -l `which cp`
        file $(ls -d /usr/bin/* | grep zip)
        echo "$USER $((2+2)) $(cal)"

    ---

        $ echo $(cal)
        October 2020 Su Mo Tu We Th Fr Sa 1 2 3 4 5  6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
        
        $ echo "$(cal)"
            October 2020      
        Su Mo Tu We Th Fr Sa  
                    1  2  3  
        4  5  6  7  8  9 10  
        11 12 13 14 15 16 17  
        18 19 20 21 22 23 24  
        25 26 27 28 29 30 31 

        $ echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER
        text /home/mirage/*.txt a b foo 4 mirage
        
        $ echo "text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER"
        text ~/*.txt {a,b} foo 4 mirage
        
        $ echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'
        text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER

    ---

        echo "The balance for user $USER is: \$5.00"
        sleep 10; echo -e "Time's up\a"
        sleep 10; echo "Time's up" $'\a'

    Adding the `-e` option to `echo` enables interpretation of escape sequences. Escape sequences may also be placed inside `$' '`.

7. **History expansion**:

        history | grep keyword
        !NN

    Bash will expand, say, `!88` into the contents of the 88th line in the history list.

    To start incremental search press `Ctrl-r` followed by the text we are looking for. When we find it, we can either press Enter to execute the command or press `Ctrl-j` to copy the line from the history list to the current command line. To find the next occurrence of the text (moving “up” the history list), press `Ctrl-r` again. To quit searching, press either `Ctrl-g` or `Ctrl-c`.

## References

* [The Linux Command Line](http://linuxcommand.org/tlcl.php)
* http://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html