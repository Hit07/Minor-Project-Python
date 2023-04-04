#----NUMBER GUESSING GAME---------------
from random import randint
from Guessing_art import logo
def level(chosen_level,number):
    i=10
    j=5
    found = False
    if chosen_level=="easy":
        while found==False:
            guess_number = int(input("Make a guess:"))
            print(f"You have {i} attempts remaining to guess the number.")
            if guess_number==number:
                print("You guess it right")
                found = True
            if i==0:
                break
            elif guess_number > 2*number:
                print("Too high")
            elif guess_number < (number/2):
                print("Too low")
            elif guess_number in range(number-10,number+10):
                 print("Very near to number in the range of 10")
            else:
                print("Nearing the number")
            i -= 1
    if chosen_level == "hard":
        while found == False:
            guess_number = int(input("Make a guess:"))
            print(f"You have {j} attempts remaining to guess the number.")
            if guess_number == number:
                print("You guess it right")
                break
            if i == 0:
                break
            elif guess_number > 2 * number:
                print("Too high")
            elif guess_number < (number / 2):
                print("Too low")
            elif guess_number in range(number - 10, number + 10):
                if guess_number > abs(number-10):
                    print("Very near to number in the forwarding range of 10")
                else:
                    print("Very near to number in the forwarding range of 10")
            else:
                print("Nearing the number")
            j -= 1

number = randint(1,100)
print(number)
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
chosen_level = input("Choose a difficulty.Type 'easy' or 'hard':").lower()
level(chosen_level,number)