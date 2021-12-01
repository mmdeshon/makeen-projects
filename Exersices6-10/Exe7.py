# defining a function to take a list of string from user and order them by length.
def exe7():

    # taking a number of elements that user is going yo have in list
    elements = int(input("How many elements are you going to add? \n"))
    user_list = []
    for i in range (0,elements):
        # taking elements from user, one by one and append them to a blank list
        user_value = input(f'enter the value number {i+1} \n')
        user_list.append(user_value)

    # sort user_list by length of each string
    user_list.sort(key = len)
    print (user_list)

# calling function
exe7()