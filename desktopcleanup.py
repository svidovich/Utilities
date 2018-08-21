# /usr/bin/env python
import os
ls = os.listdir(".")
pwd = os.getcwd()
print(ls)
print(pwd)
if 'images' not in ls:
	os.mkdir("images")
if 'archives' not in ls:
	os.mkdir("archives")
if 'books' not in ls:
	os.mkdir("books")
if 'scripts' not in ls:
	os.mkdir("scripts")

