import random

roll_quit = input("Press r to roll or q to quit: ".casefold())

while roll_quit == "q" or "Q": 
    print("Thank you for playing!")
    break


while roll_quit == "r" or roll_quit == "R":
    random_dice_one = random.randint(1,6)
    random_dice_two = random.randint(1,6)
    print(random_dice_one)
    print(random_dice_two)
    play_again = input("If you wish to roll again press r, to quit press q: ")
    if play_again == "q" or play_again == "Q":
        print("Thank you for playing!")
        break



