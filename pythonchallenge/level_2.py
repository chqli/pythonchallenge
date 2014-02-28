def count_chars():
	with open ("dump.txt", "r") as myfile:
		data=myfile.read().replace('\n', '')

	dnary={}
	for char in data:
		if(char in dnary):
			dnary[char]+=1
		else:
			dnary[char]=1
	print (sorted(dnary.items(), key=lambda x: x[1],reverse=True))

count_chars()
#http://www.pythonchallenge.com/pcc/def/equality.html
#http://www.pythonchallenge.com/pc/def/ocr.html
#http://www.pythonchallenge.com/pc/def/map.html