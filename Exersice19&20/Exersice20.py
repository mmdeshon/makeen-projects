from random import randint
pc_num = randint(1, 11)
guess_count = 0
print('*' * 40)
print(pc_num)
print('     Welcome to my Number Guess game :) \nI Have selected a random number between(1-10).')
while guess_count < 4:

    print(f'**You have "{4-guess_count}" chances left.**')
    user_guess = int(input('What is your guess? \n'))

    if pc_num == user_guess:
        if guess_count == 0:
            print("OMG!!!, You find out right number in your 'first' guess. Such a genius you are!")
            break
        else:
            print(f'Wow! You find the correct number after {guess_count+1} times')
            break

    else:
        print('*' * 40)
        if guess_count == 2:
            print("Watch Yourself. It's your last chance.")
        elif guess_count == 3:
            print("Game Over!. Better luck next time.")
            break
        else:
            print('Wrong Guess! Try again.')
        guess_count += 1
