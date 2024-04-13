#here we had imported random module of python
import random

rock='✊'
paper='🫲'
scissor='✌️'
game_images=[rock,paper,scissor]
user_choice=int(input("Enter Your choice Rock(0) Paper(1) Scissor(2) :"))

if user_choice>=3 or user_choice<0:
    print("Enter a valid choice")
else:
    print(f"You had entered {game_images[user_choice]}")
    comp_choice=random.randint(0,2)
    print(f"Computer choice is {game_images[comp_choice]}")

    if(comp_choice==0 and user_choice==2):
        print("You loose")
    elif(user_choice==0 and comp_choice==2):
        print("You win")
    elif(comp_choice>user_choice):
        print("You loose")
    elif(user_choice>comp_choice):
        print("You win")
    elif(user_choice==comp_choice):
        print("It's a draw")
