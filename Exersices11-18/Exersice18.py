def age_check():
    user_age = int(input('How old are you: \n'))
    if user_age < 18:
        print('You are not allowed to have driving license')
    else:
        print('You can have a driving license')


age_check()