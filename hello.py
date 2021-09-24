#!/usr/bin/env python3
import os
from templates import login_page
from templates import secret_page
import cgi
import secret
import sys
# print('Set-Cookie:UserID = XYZ;\r\n')
# print('Set-Cookie:Password = XYZ123;\r\n')
# print('SET-Cookie:Expires = Tuesday, 31-Dec-2100 23:12:40')
# print(os.environ)
print(login_page())
# posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
# if posted_bytes:
#     posted = sys.stdin.read(int(posted_bytes))
#     print(f"<p> POSTED: <pre>")
#     for line in posted.splitlines():
#         print(line)
#     print("</pre></p>")


form = cgi.FieldStorage()

if len(form) > 0:
    name = form["username"].value
    pw = form["password"].value

    if name == secret.username and pw == secret.password:
        print('Set-Cookie:UserID = %s;\r\n' % name)
        print('Set-Cookie:Password = %s;\r\n' % pw)
        print('SET-Cookie:Expires = Tuesday, 31-Dec-2100 23:12:40')
        
        print(secret_page(name, pw))
