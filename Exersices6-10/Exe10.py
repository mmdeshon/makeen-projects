def Exe10():
	user_input = input('Enter a number plz: \n')
	blank_list =[]
	for index,digit in enumerate(user_input):
		blank_list.append(digit)
		blank_list.sort(reverse = True)
	for index,digit in enumerate(blank_list):
		if index == 0:
			num_str = digit
		else:
			num_str +=  digit
	print(int(num_str))

Exe10()
