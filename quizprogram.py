print('Welcome to the Quiz Game')
playing = input("Do Want to Play? ")
print(playing)
score=0
total_questions=5
if playing != 'yes':
    quit()
else:
    print("Let's Play...")
    
    
    print('1. Google is:')
    print('a) A Browser')
    print('b) A Search Engine')
    answer = input("Choose the correct answer (a/b): ").lower()
    if answer == 'b':
        print("Correct")
        score += 1
    else:
        print("Incorrect")


    print('2. Who is the founder of Facebook?')
    print('a) Elon Musk')
    print('b) Mark Zuckerberg')
    print('c) Bill Gates')
    answer = input("Choose the correct answer (a/b/c): ").lower()
    if answer == 'b':
        print("Correct")
        score += 1
    else:
        print("Incorrect")


    print('3. ROM stands for:')
    print('a) Random Only Memory')
    print('b) Read Open Memory')
    print('c) Read Only Memory')
    answer = input("Choose the correct answer (a/b/c): ").lower()
    if answer == 'c':
        print("Correct")
        score += 1
    else:
        print("Incorrect")

 
    print('4. RAM stands for:')
    print('a) Random Access Memory')
    print('b) Read Access Memory')
    print('c) Random Actual Memory')
    answer = input("Choose the correct answer (a/b/c): ").lower()
    if answer == 'a':
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    

    print('5. Printer is an example of which types of device, Output or Input? ')
    print('a) Output')
    print('b) Storage')
    print('c) Input')
    answer = input("Choose the correct answer (a/b/c): ").lower()
    if answer == 'a':
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    
    print('Total Score ' +str(score))
    percentage = (score / total_questions) * 100
    print('percentage : '+ str(percentage)+'%')

    if percentage >= 80:
       print("Congratulations! \U0001F389 \U0001F44F You did amazing!")

    elif 50 <= percentage < 80:
        print('Good Job! \N{grinning face} Keep it up!')
    else:
        print('Better Luck Next Time! \N{worried face}')