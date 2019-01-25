#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password
import os

# if "HTTP_COOKIE" in os.environ:
#    for cookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
#       (key, value ) = split(cookie, '=')
#       if key == "username":
#          c_username = value
#       if key == "password":
#          c_password = value

print("Content-Type: text/html")

c_username = ""
c_password = ""

try:
    cookie_string = os.environ.get("HTTP_COOKIE")
    cookie_pairs = cookie_string.split(";") # gives me ["key=val"]
    for pair in cookie_pairs:
        key, val = pair.split("=")
        if "username" in key:
            c_username = val
        elif "password" in key:
            c_password = val
except:
    pass

if c_username and c_password:
    print("\n\n")
    # print("<h1>" + os.environ.get("HTTP_COOKIE") + "</h1>")
    print(secret_page(c_username, c_password))
elif os.environ.get("REQUEST_METHOD", "GET") == "POST":
    # print form post data
    form = cgi.FieldStorage()
    f_username = form.getvalue("username")
    f_password = form.getvalue("password")
    if f_username == username and f_password == password:
        print("Set-Cookie: username={};".format(username))
        print("Set-Cookie: password={}".format(password))
        print("\n\n")
        print(secret_page(username, password))
    else:
        print("\n\n")
        print(after_login_incorrect())
else:
    print("\n\n")
    # print("<h1>" + os.environ.get("HTTP_COOKIE") + "</h1>")
    print(login_page())
