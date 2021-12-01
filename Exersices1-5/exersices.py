ex_num = int(input("Which exersice are you going to do? \n"))



def ex1():
    elements = int(input("How many elements are you going to add? \n"))
    user_list = []
    for i in range (0,elements):
        user_value = input(f'enter the value number {i+1} \n')
        user_list.append(user_value)
    user_list.reverse()
    print (user_list)

def ex2():
    elements = int(input("How many elements are you going to add? \n"))
    user_list = []
    for i in range(0, elements):
        user_value = int(input(f'enter the value number {i + 1} \n'))
        user_list.append(user_value)
    user_list.sort()
    print(user_list[-2:])


def ex3():
    elements = int(input("How many elements are you going to add? \n"))
    user_list = []
    for i in range(0, elements):
        user_value = int(input(f'enter the value number {i + 1} \n'))
        user_list.append(user_value)
    user_list.reverse()
    print(user_list)


def ex4():
    user_num = input('Enter a number:\n')
    my_list = []
    for i in range(0,len(user_num)):
        x = int(user_num[i])
        my_list.append(x)
    my_list.sort()
    print(my_list[-1])




def ex5():
    my_list = [1,2,'a','b']
    int_list = []
    for i in my_list:
        if type(i) == int:
            int_list.append(i)
    print(int_list)



if ex_num == 1:
    ex1()
if ex_num == 2:
    ex2()
if ex_num == 3:
    ex3()
if ex_num == 4:
    ex4()
if ex_num == 5:
    ex5()

