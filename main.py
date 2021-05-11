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
#Create a list of choices
rps = [rock,paper,scissors]

#Get player player_choice and cast it to an integer
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if player_choice >= 3 or player_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  #Print player player_choice
  print(rps[player_choice])

  print("Computer chose:")
  #Get computer player_choice
  computer_choice = random.randint(0,2)

  #Print computer player_choice
  print(rps[computer_choice])

  #Check result
  if player_choice == computer_choice:
    print("It is a draw")
  elif (player_choice== 0 and computer_choice == 2) or (player_choice > computer_choice):
    print("You win")
  elif (player_choice== 2 and computer_choice == 0) or (player_choice <computer_choice) :
    print("You lose")


print("-\nThis repl has exited, run again?")

