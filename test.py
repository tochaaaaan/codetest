"""
このファイルに解答コードを書いてください
"""
 
text_str = input()
def extend_fizzbuzz(text_str):
	text = open(text_str).read()
	box = text.splitlines()
	#print(box)	
	max_index = len(box)-1
	ret_box={}
	for i in range(max_index-1):
		temp=[]
		temp = box[i].split(":")
		if int(box[max_index])%int(temp[0])==0:
			ret_box[int(temp[0])]=temp[1]	
	if ret_box == {}:
		print(box[max_index])
	else:
		ret_string=""
		sort_item = sorted(ret_box.items())
		for i in sort_item:
			ret_string += i[1]
		print(ret_string)
extend_fizzbuzz(text_str);	
	
