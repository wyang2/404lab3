#!/usr/bin/env python3
import cgi
# import cgitb
# cgitb.enable()
import os
import json
from urllib.parse import parse_qs

print("Content-Type: text/html\n")
print()
print("<!doctype html>")
print("<head>")
print("<title>Hello</title>")
print("<style>pre {white-space: pre-wrap; word-wrap: break-word;}</style>")
print("</head>")
print("<h2>Hello World</h2>")

# print query params
print("<dl>")
print("<dt>QUERY_STRING:</dt>")
print("<dd>")
print(parse_qs(os.environ.get("QUERY_STRING")))
print("</dd>")
print("<dt>HTTP_USER_AGENT:</dt>")
HTTP_USER_AGENT = os.environ.get("HTTP_USER_AGENT", None)
print("<dd>" + HTTP_USER_AGENT + "</dd>")
print("</dl>")

# cgi.print_environ()
print("<pre>")
env_json = {}
for key, value in os.environ.items():
    env_json[key] = value
print(json.dumps(env_json))
print("</pre>")

#q1: cgi print environment
# os.environ

#q2: query parameter: thing in url, after hello world/?name = yangwenhan

#q3: HTTP_USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",

#q5: line 36 "Set - Cookie"
#q6: send http 1.1 request
#q7: 
