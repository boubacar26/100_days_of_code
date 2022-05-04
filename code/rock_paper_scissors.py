import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_choice = input("What do you choose? Tyoe 0 for Rock, 1 for Paper or 2 for Scissors. ")
computer_choice = random.randint(0, 2)
player_choice = int(player_choice)


if player_choice == 1 and computer_choice == 0:
  print(f"You choose \n: {paper}")
  print(f"The computer choose: \n {scissors} \n You lose")
elif player_choice == 1 and computer_choice == 2:
  print(f"You choose: \n {paper}")
  print(f"The computer choose: \n {rock} \n You Win")
elif player_choice == 1 and computer_choice == 1:
  print(f"You choose: \n {paper}")
  print(f"The computer choose:\n{paper} \n It's a Draw")
elif player_choice == 0 and computer_choice == 1:
  print(f"You choose:\n {rock}")
  print(f"The computer choose:\n {paper} \n You Lose")
elif player_choice == 0 and computer_choice == 2:
  print(f"You choose:\n {rock}")
  print(f"The computer choose:\n{scissors} \n You Win")
elif player_choice == 0 and computer_choice == 0:
  print(f"You choose:\n{rock}")
  print(f"The computer choose:\n{rock} \n It's a Draw")
elif player_choice == 2 and computer_choice == 1:
  print(f"You choose:\n{scissors}")
  print(f"The computer choose:\n{rock} \n You Lose")
elif player_choice == 2 and computer_choice == 0:
  print(f"You choose:\n{scissors}")
  print(f"The computer choose:{paper} \n You Win")
elif player_choice == 2 and computer_choice == 2:
  print(f"You choose:\n{scissors}")
  print(f"The computer choose:{scissors} \n It's a draw")
else:
    print("You choose a wrong number.")