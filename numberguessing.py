import random
top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <=0 :
        print('pls type a larger number')
        quit()
else:
    print('pls type a number')
    quit()

random_num =random.randint(0,top_of_range)
guess =0

while True:
    guess += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('pls type a number')
        continue

    if user_guess == random_num:
        print('You got it')
        break
    elif user_guess > random_num:
        print('You were above the number')
    else:
        print('You were below the number')

print("you got it in", guess , "guesses")
    

