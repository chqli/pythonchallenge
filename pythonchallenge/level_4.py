import urllib.request,re


data=63579;
Url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
pattern=re.compile(r'(\D+)(\d+).*')
print(pattern.match('and the next nothing is 45439').group(2))
while True:
	url=Url+str(data)
	print(url)
	response = urllib.request.urlopen(url)
	parsedValue=str(response.read().decode('utf-8'))
	print(parsedValue)
	validMatch=re.search(r'\d+', parsedValue)
	if validMatch:
		data=validMatch.group(0)
	else:
		break
print ('done')
#http://www.pythonchallenge.com/pc/def/peak.html