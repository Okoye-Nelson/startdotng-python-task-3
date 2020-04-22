import random

print('Hello there! You are about to participate in a guessing game. Are you up for it?\n')
value = str(input("Type 'YES' to proceed or 'NO' to exit if you're not interested: "))
user_input = value.upper()
if user_input == "YES":
    print('''\nGreat!
So the game goes like this, there are 3 level options:
     1 - Easy, with 6 guess tries available, you must guess a number between 1 - 10.
     2 - Medium, with 4 guess tries available, you must guess a number between 1 - 20.
     3 - Hard, with 3 guess tries available, you must guess a number between 1 - 50.''')

    level_choice = int
    while True:
        try:
            number_select = int(input('\nWhich level do you want to play?: '))
            break
        except ValueError:
            print("Sorry, but you need to input a number value")
    while number_select <= 0 or number_select >= 4:
        try:
            number_select = int(input("Kindly input a number value between 1 to 3: "))
        except TypeError:
            print("You typed in an unspecified number")
    else:
        level_choice = number_select

    if level_choice == 1:
        print("\nAlright. Easy level. Leggo!")
        secret_number = random.randrange(1, 10)  # randomly select value from specified range
        guess_count = 0
        guess_attempts = 6
        guess_limit = 5
        while guess_count <= guess_limit:
            guess = int(input("What is your guess number: "))
            guess_count += 1
            guess_attempts -= 1
            if guess != secret_number:
                print("That was wrong. Try again buddy. You have " + str(guess_attempts), "attempt(s) left")
            else:
                print("You got it right. You win!")
        else:
            print("Lo siento, you failed. Try again!")

    elif level_choice == 2:
        print("\nAlright. Medium level. Leggo!")
        secret_number = random.randrange(1, 20)  # randomly select value from specified range
        guess_count = 0
        guess_attempts = 4
        guess_limit = 3
        while guess_count <= guess_limit:
            guess = int(input("What is your guess number: "))
            guess_count += 1
            guess_attempts -= 1
            if guess != secret_number:
                print("That was wrong. Try again buddy. You have " + str(guess_attempts), "attempt(s) left")
            else:
                print("You got it right. You win!")
        else:
            print("Lo siento, you failed. Try again!")

    elif level_choice == 3:
        print("\nAlright. Hard level. Leggo!")
        secret_number = random.randrange(1, 50)  # randomly select value from specified range
        guess_count = 0
        guess_attempts = 3
        guess_limit = 2
        while guess_count <= guess_limit:
            guess = int(input("What is your guess number: "))
            guess_count += 1
            guess_attempts -= 1
            if guess != secret_number:
                print("That was wrong. Try again buddy. You have " + str(guess_attempts), "attempt(s) left")
            else:
                print("You got it right. You win!")
        else:
            print("Sorry, you failed. Game over!")

elif user_input == "NO":
    print("\nAlright, maybe some other time. Bye!")

else:
    print("\nSorry, you typed in a wrong option. Try again.")
