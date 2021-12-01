# defining a function to take a number list from a user and check if sum is odd or even.
def ex6():

    # taking a number of elements that user is going yo have in list
    elements = int(input("How many elements are you going to add? \n"))

    num_list = []
    for i in range(0, elements):
        # taking elements from user, one by one and append them to a blank list
        user_value = int(input(f'enter the value number {i + 1} \n'))
        num_list.append(user_value)

    num_sum = 0
    for num in num_list:
        num_sum += num

    # check if num_sum is odd or even
    if num_sum % 2 == 0:
        print (f"the sum is {num_sum}, so it's ((even))")
    else:
        print(f"the sum is {num_sum}, so it's ((odd))")

# calling function
ex6()
