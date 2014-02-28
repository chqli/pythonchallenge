import pprint,pickle

banner = pickle.load(open('banner.p','rb'))
pprint.pprint(banner)

data=''
for item in banner:
	for (char,times) in item:
		data=data+''.join(char*times)
	data+='\n'
print(data)
#http://www.pythonchallenge.com/pc/def/channel.html