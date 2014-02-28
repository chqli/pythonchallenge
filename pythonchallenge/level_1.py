def para_remap():
	alphabet=list('abcdefghijklmnopqrstuvwxyz')
	dnary=remap(alphabet)
	test_string= """map"""
	test_list=list(test_string)

	for i,char in enumerate(test_list):
		if (char in dnary):
			test_list[i]=dnary[char]
	return ''.join(test_list)

def remap(mylist):
	mydict={}
	for i,char in enumerate(mylist):
		mydict[char]=mylist[(i+2)%26]

	return mydict
print(para_remap())




