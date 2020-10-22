# SSH: Port 22

1. SSH private keys are usually stored in the path `C:\Users\username\.ssh\id_rsa`
2. If a private key could be fetched successfully, it could be used to login into the server

        chmod 400 id_rsa
        ssh username@10.10.10.4 -i id_rsa
