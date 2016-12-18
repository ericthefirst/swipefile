#!/usr/bin/python 

import os;
import cgitb;
import cgi;
import sys;

cgitb.enable()

IMG_DIR = "img"

print("Content-type: text/html\r\n\r\n")
print """
<html>
	<head>
		<title>Swipe file</title>
		<meta charset='utf-8'>

		<style>

			table,thead,th,td { 
				border: none;
				border-collapse: collapse;
			}

			body {
				background-color: #339999;
			}

			table {
				background-color: #00aa88;
			}

			tr.title {
				background-color: #55bbdd;
			}

			tr.title > td {
				padding: 15px 10px 10px 15px;
			}

			td { 
				padding: 15px 20px 0px 0px;
				font-size: 40px;
			}

			.title {
				font-family: Helvetica;
				font-size: 60;
			}

			tr.title > td {
				font-size: 60px;
			}

			tr.data > td {
				padding-bottom: 80px
			}

			.comments {
				vertical-align: text-top;
			}

	a, a:visited {
		text-decoration: none;
		color: #174bb3;
	}

	#upload { 
		padding: 10px;
		position: fixed;
		right: 10px;
		bottom: 10px;
		color: white;
		font-family: Helvetica, Arial, sans-serif;
		font-size: 14px;
		text-decoration: none;
		background-color: rgba(28, 180, 240, .5 );
		border: 3px solid rgba(20, 240, 220, .9);
	}

		</style>
	</head>
	<body>
		<table>
"""

with open("records", 'r') as f:
	lines = f.readlines()
lines.reverse()

for line in lines:
	tokens  = line.split('\t')
	title    = tokens[0]
	comments = tokens[1]
	print('\t\t\t<tr class="title"><td colspan="2">{0}</td></tr><tr class="data"><td><img style="width:400px" src="{1}/{2}"></td><td class="comments">{3}</td></tr></div>'.format(title, IMG_DIR,title + ".png", comments))

print """
		</table>
		<a id='upload' href='upload/upload_portal.html'>Upload more</a>
	</body>
</html>"""

