import random
item_list = ["rock", "paper", "scissor"]

user_choice = input("enter your move = rock, paper, scissor=")
computer_choice = random.choice(item_list)

print(f"user choice is {user_choice}, computer choice is {computer_choice} ")
if user_choice == computer_choice:
    print("It's a draw =  both choices are same")
elif user_choice == "rock":
    if computer_choice == "paper":
         print("paper covers rock = computer win")
    else:
        print("rock smashes scissor = you win ")
elif user_choice == "paper":
    if computer_choice == "scissor":
        print("scissor cuts paper = computer win")
    else:
        print("paper covers rock =  you win")
elif user_choice == "scissor":
    if computer_choice == "paper":
        print("scissor cuts paper = you win")
    else:
        print("rock smashes scissor = computer win")