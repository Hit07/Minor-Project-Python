from Higher_lower_Start_art import list_people
from Higher_lower_Start_art import logo_1
from Higher_lower_Start_art import logo_vs
from random import choice
print("--------------------------------------\n"+logo_1+"-----------------------------------------\n")
def game():
    score = 0
    play_game = True
    choose_b = choice(list(list_people.keys()))
    while play_game:
        choose_a = choose_b
        if choose_a == choose_b:
            choose_a = choose_b
            choose_b = choice(list(list_people.keys()))
        # print(list_people[choose_a],list_people[choose_b])
        print(f"Compare A: {choose_a}")
        print(logo_vs)
        print(f"Against B: {choose_b}")
        guess = input("\nWho has more followers Type 'A' or 'B':").lower()
        if guess =='a' and list_people[choose_a]<list_people[choose_b]:
            score += 1
            print(f"\nGood Job!,Right answer....Final Score: {score}")
        elif guess == 'b' and list_people[choose_a]>list_people[choose_b]:
            score += 1
            print(f"\nGood Job!,Right answer....Final Score: {score}")
        else:
            print(f"\nSorry,that's wrong answer.Final Score: {score}\n\nGame Over!!😓")
            play_game = False

input_1 =input("Wanna play the game:Type 'yes' or 'no':--").lower()
if input_1 == 'yes':
    game()
else:
    print("Try once!!")
