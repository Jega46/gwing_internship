import random

user_wins =0
comp_wins =0

option = ['rock','paper','scissors']

while True:
    user_input = input("Type a input(rock/paper/scissors/quit): ").lower()

    if user_input == 'quit':
        break

    if user_input not in option:
        continue

    random_number = random.randint(0,2)
    comp_input = option[random_number]
    print("Computer picks : ",comp_input)

    if user_input == 'rock' and comp_input == 'scissors':
        print('You won')
        user_wins+=1
        print("Computer Score: ", comp_wins)
        print("User Score: ", user_wins)
    elif user_input == 'paper' and comp_input == 'rock':
        print('You won')
        user_wins+=1
        print("Computer Score: ", comp_wins)
        print("User Score: ", user_wins)
    elif user_input == 'scissors' and comp_input == 'paper':
        print('You won')
        user_wins+=1
        print("Computer Score: ", comp_wins)
        print("User Score: ", user_wins)
    else:
        print('computer wins')
        comp_wins+=1
        print("Computer Score: ", comp_wins)
        print("User Score: ", user_wins)

print('Number of user wins : ',user_wins)
print('Number of computer wins : ',comp_wins)
if user_wins==comp_wins:
    print("same are Winners! Congratulations! \U0001F389 \U0001F44F ")
elif user_wins <=comp_wins:
     print("Computer Wins! Congratulations! \U0001F389 \U0001F44F ")
else :
    print("User Wins! Congratulations! \U0001F389 \U0001F44F You did Amazing! ")

print("Goodbye")