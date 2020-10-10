# IIS Short File Name Disclosure 

**.Net** websites are vulnerable to **direct URL access**. An attacker can possibly find important files and folders that are not normally visible.

1. Download [IIS Shortname Scanner](https://github.com/irsdl/IIS-ShortName-Scanner.git)
2. Check if target is vulnerable

        $ java -jar iis_shortname_scanner.jar http://example.com/folder/

3. If found vulnerable, run a scan to find any sensitive file on the server 

        $ java -jar iis_shortname_scanner.jar 2 20 http://example.com/folder/new%20folder/

4. Once a shortname is identified successfully for a file, e.g., `ABC_DE~1.TXT`, then guess rest of the file name.

## References

* https://soroush.secproject.com/blog/tag/iis-tilde-vulnerability/