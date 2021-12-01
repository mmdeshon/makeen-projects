# Definig Our function That take 'user_list' and 'limit
def LimitCheck(user_list, limit):
	#Sort numbers to fing the biggest one
	user_list.sort()
	
	# Check if the biggest number of list is bigger than limit or not
	if user_list[-1] <= limit:
		print('True')
	else:
		print('Flase')
				
# Calling Function
LimitCheck([2, 7, 7], 7)