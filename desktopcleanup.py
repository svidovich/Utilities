# /usr/bin/env python
import os
ls = os.listdir(".")
pwd = os.getcwd()

if 'images' not in ls:
	os.mkdir("images")
if 'archives' not in ls:
	os.mkdir("archives")
if 'books' not in ls:
	os.mkdir("books")
if 'scripts' not in ls:
	os.mkdir("scripts")

for result in ls:
	if any(x in result for x in['jpg', 'png', 'gif', 'tif']):
		current = os.path.join(pwd, result)
		moved = os.path.join(pwd, 'images', result)
		os.rename(current, moved)

for result in ls:
	if any(x in result for x in['.zip', '.gz', '.tar', '.bz2', '.lz', '.7z', '.cab', '.jar', '.rar', '.tgz', '.zipx']):
		current = os.path.join(pwd, result)
		moved = os.path.join(pwd, 'archives', result)
		os.rename(current, moved)
