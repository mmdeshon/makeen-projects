def create_phone_number(my_list):
    num_str = ('( ')
    for index, digit in enumerate(my_list):
        num_str += str(digit)
        if index == 2:
            num_str += (') ')
        if index == 5:
            num_str += ('-')
    print(num_str)


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
