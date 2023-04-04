import random
choice = int(input("What do you choose?Type 0 for Rock, 1 for for Paper or 2 for Scissors."))
comp_choice = random.randint(0,2)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if (choice == 0) and (comp_choice == 1):
  print(f"Your choice : {rock}")
  print(f"Computer choice : {paper}")
  print("You loose")
elif (choice == 1) and (comp_choice == 2):
  print(f"Your choice : {paper}")
  print(f"Computer choice : {scissors}")
  print("You loose")

elif (choice == 1) and (comp_choice == 0):
  print(f"Your choice : {paper}")
  print(f"Computer choice : {rock}")
  print("You win")
elif (choice == 2) and (comp_choice == 1):
  print(f"Your choice : {scissors}")
  print(f"Computer choice : {paper}")
  print("You win")
else:
  print("Draw")


