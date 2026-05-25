import random

rock = '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
'''

paper = '''
    ___
---'   _)_
          __)
          ___)
         ___)
---.____)
'''

scissors = '''
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
'''

game_images = [rock, paper, scissors]

while True:
    user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

    if user_choice >= 3 or user_choice < 0:
        print("Invalid choice!")
        continue

    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)

    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a Draw!")
    elif (
        (user_choice == 0 and computer_choice == 2) or
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == 2 and computer_choice == 1)
    ):
        print("You Win!")
    else:
        print("You Lose!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Game Over!")
        break
