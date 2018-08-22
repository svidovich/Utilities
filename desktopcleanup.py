# /usr/bin/env python
import os
ls = os.listdir(".")
pwd = os.getcwd()

if 'images' not in ls:
	os.mkdir("images")
if 'archives' not in ls:
	os.mkdir("archives")
if 'documents' not in ls:
	os.mkdir("documents")
if 'scripts' not in ls:
	os.mkdir("scripts")
if 'music' not in ls:
	os.mkdir("music")


for result in ls:
	if any(x in result.lower() for x in['jpg', 'png', 'gif', 'tif']):
		current = os.path.join(pwd, result)
		moved = os.path.join(pwd, 'images', result)
		os.rename(current, moved)

for result in ls:
	if any(x in result for x in['.zip', '.gz', '.tar', '.bz2', '.lz', '.7z', '.cab', '.jar', '.rar', '.tgz', '.zipx']):
		current = os.path.join(pwd, result)
		moved = os.path.join(pwd, 'archives', result)
		os.rename(current, moved)

for result in ls:
	if any(x in result for x in['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt']):
		current = os.path.join(pwd, result)
		moved = os.path.join(pwd, 'documents', result)
		os.rename(current, moved)

for result in ls:
	if any(x in result for x in['.sh', '.ps1', '.x']):
		current = os.path.join(pwd, result)
		moved = os.path.join(pwd, 'scripts', result)
		os.rename(current, moved)

for result in ls:
	if any(x in result for x in['.wav', '.ogg', '.mp3', '.flac', '.m4a','.wma','.vox']):
		current = os.path.join(pwd, result)
		moved = os.path.join(pwd, 'music', result)
		os.rename(current, moved)
