# MSRPC: Port 135

* List the interface IDs (IFID) using [rpcdump](https://resources.oreilly.com/examples/9780596510305/tree/master/tools/rpctools)

        rpcdump.py -port 135  10.10.10.4
        
* Identify any interesting **RPC interfaces** by analysing at the **named pipes**. Example, `\pipe\atsvc` would indicate presence of a **task scheduler**, that could be used to execute commands remotely.

## References

* https://book.hacktricks.xyz/pentesting/135-pentesting-msrpc
