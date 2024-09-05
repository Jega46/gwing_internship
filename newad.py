name = input("Enter your name : ")
print('Welcome ',name,' to this new adventure game')

ans = input('Make choice whether you want go to mountain or river : ').lower()

if ans == 'mountain':
    print("You head towards the mountains and encounter a friendly traveler.")
    print("The traveler offers to guide you to a hidden treasure or you can continue exploring on your own.")
    choice = input("Enter 'treasure' or 'explore': ").lower()

    if choice == 'treasure':
        print("The traveler guides you to the hidden treasure. Congratulations, you win!")
    elif choice == 'explore':
        print("You get lost in the mountains and end up spending the night there. Better luck next time!")
    else:
        print('Not a valid option.You lose')


elif ans == 'river':
    print("You walk towards the river and see a small boat.")
    print("You can either take the boat across the river or follow the riverbank.")
    choice = input("Enter 'boat' or 'bank': ").lower()

    if choice=='boat':
         print("You take the boat and find a beautiful island with a hidden cave full of jewels. Congratulations, you win!")
    elif choice=='bank':
         print("Following the riverbank, you find a peaceful village and decide to settle there. Congratulations, you win!")
    else:
        print("Not avalid option.You lose")
else:
    print('Not a valid option. You lose')