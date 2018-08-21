# /usr/bin/env python
import os
ls = os.listdir(".")
print(ls)

if 'images' not in ls:
	os.mkdir("images")
