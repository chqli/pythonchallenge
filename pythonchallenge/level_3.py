import string,re
def count_chars():
	with open ("dump.txt", "r") as myfile:
		data=myfile.read().replace('\n', '')

	validMatch=re.findall(r"[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]",data)
	print(len(validMatch))
	if(validMatch):
		for text in validMatch:
			print(text[4])
count_chars()
#http://www.pythonchallenge.com/pc/def/linkedlist.php
#http://www.pythonchallenge.com/pc/def/linkedlist.html
