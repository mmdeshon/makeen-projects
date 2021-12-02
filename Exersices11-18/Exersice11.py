def CountVowels():
    user_input = input('Enter a word plz: \n')
    count = 0
    for letter in user_input:
        if letter in ['a', 'e', 'i', 'u', 'o']:
            count += 1
    if count == 0:
        print(f'There is no vowel in "{user_input}"')
    elif count == 1:
        print(f'There is on vowel in "{user_input}"')
    else:
        print(f'There are {count} vowels in "{user_input}"')

CountVowels()