# Impacket Tools

1. Download latest release of **Impacket** from [SecureAuthCorp/impacket GitHub](https://github.com/SecureAuthCorp/impacket) repository

        $ wget https://github.com/SecureAuthCorp/impacket/releases/download/impacket_0_9_21/impacket-0.9.21.tar.gz
        $ tar zxvf impacket-0.9.21.tar.gz
        $ cd impacket-0.9.21

2. Create a Python virtual environment
   
        $ python3 -m venv /path/to/new_virtual_environment
        $ source /path/to/new_virtual_environment/bin/activate

3. Setup the environment

        $ python -m pip install .

4. Start using the Python tools that are available inside the **examples** folder 

        $ ./examples/mssqlclient.py 
        Impacket v0.9.21 - Copyright 2020 SecureAuth Corporation

        usage: mssqlclient.py [-h] [-port PORT] [-db DB] [-windows-auth] [-debug] [-file FILE] [-hashes LMHASH:NTHASH] [-no-pass]
                            [-k] [-aesKey hex key] [-dc-ip ip address]
                            target

        TDS client implementation (SSL supported).

        positional arguments:
        target                [[domain/]username[:password]@]<targetName or address>

        optional arguments:
        -h, --help            show this help message and exit
        -port PORT            target MSSQL port (default 1433)
        -db DB                MSSQL database instance (default None)
        -windows-auth         whether or not to use Windows Authentication (default False)
        -debug                Turn DEBUG output ON
        -file FILE            input file with commands to execute in the SQL shell

        authentication:
        -hashes LMHASH:NTHASH
                                NTLM hashes, format is LMHASH:NTHASH
        -no-pass              don't ask for password (useful for -k)
        -k                    Use Kerberos authentication. Grabs credentials from ccache file (KRB5CCNAME) based on target
                                parameters. If valid credentials cannot be found, it will use the ones specified in the command line
        -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256 bits)
        -dc-ip ip address     IP Address of the domain controller. If ommited it use the domain part (FQDN) specified in the
                                target parameter
