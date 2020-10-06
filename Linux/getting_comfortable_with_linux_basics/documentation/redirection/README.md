# Redirection

*"Everything is a file."*

The shell references standard input, output and error file streams internally as file descriptors 0, 1, and 2, respectively.

1. Redirect **standard error**: `ls -l /bin/usr 2> ls-error.txt`
2. Redirect both **standard output and standard error**: `ls -l /bin/usr > ls-output.txt 2>&1`
    1st, redirect standard output to a file, and then redirect file descriptor 2 (i.e., standard errror) to file descriptor 1 (i.e., standard output) using the notation **2>&1**.

   Alternative, streamlined method to redirect both standard output and standard error to a file is: 

        ls -l /bin/usr &> ls-output.txt
        ls -l /bin/usr &>> ls-output.txt
    
3. **Suppress error** messages from a command by redirecting error and status messages to a special file `/dev/null` (i.e., a *bit bucket*), which accepts input and does nothing with it: 
   
        ls -l /bin/usr 2> /dev/null
4. **Join** files: `cat file1 file2 ... fileN > combinedFile.out`
5. **Create** short text files using `cat`

        $ cat > file.txt
        Type your text here...
        Press Ctrl-d when done.

6. **Pipe** the standard output of one command to standard input of another: `ls -l /bin /usr/bin | sort | uniq | wc -l`
7. Use `uniq` with `-d` option to see the **list of duplicates**

        ls -l /bin /usr/bin | sort | uniq -d | less

8. Print **first N lines** of a file

        head -n 5 ls-output.txt

9. Print **last N lines** of a file

        ls /usr/bin | tail -n 5

10. Monitor a file in **real time**: `tail -f /var/log/messages`
11. `tee` program copies standard input to **both** standard output and one or more files

        ls /usr/bin | tee ls.txt | grep zip
