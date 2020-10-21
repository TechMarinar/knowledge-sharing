# LDAP: Port 389

1. Create a list of crendentials obtained from various machines.
2. Use these credentials with [BloodHound](https://github.com/fox-it/BloodHound.py) and make an attempt to enumerate Active Directory

        bloodhound-python -d domain.local -u USERNAME -p PASSWORD -gc pathfinder.domain.local -c all -ns 10.10.10.4

3. Configure `neo4j`

        apt install neo4j
        neo4j console

    Navigate to `http://localhost:7474/browser/` and setup database login credentials

4. Start BloodHound

        apt install bloodhound
        bloodhound --no-sandbox

5. Drag and drop the `.json` files (that were obtained in step #2, above) 
6. Once BloodHound is doen analysing the JSON files, select various queries to see the results
   1. Shortest Paths to High value Targets
   2. Find Principles with DCSync Rights
   3. etc.

    If a service account is found to have **GetChangesAll** privileges to the domain, then this account will have the ability to request replication data from the domain controller. It could be used to gain sensitive information such as user hashes.

## References

* https://latesthackingnews.com/2018/09/25/bloodhound-a-tool-for-exploring-active-directory-domain-security/
