def diamond_room():
    print("You are in Diamond room.")
    print("What would you like to do?")
    answer = input("Enter your response 1 or 2: ")
    if answer == "1":
        game_over("You were so close yet so far")
    elif answer == "2":
        print("your hard work paid off and you win!!!")
        play_again()
    else:
        game_over("You did not put the right number.")


def play_again():
    print("Do you want to play again?")
    answer = input("Enter your response: ")
    if answer == "y" or "yes":
        start()
    else:
        exit()


def bear_room():
    print("You are in bear room.What would you do?")
    print("1 Take the honey")
    print("2 Taunt the bear")
    answer = input("Enter your response: ")
    if answer == "1":
        game_over("The bear killed you.")
    elif answer == "2":
        diamond_room()
    else:
        game_over("You did not type the number correctly.")


def monster_room():
    print("You are with the monster. What would you do?")
    print("1- Fight the monster to proceed.")
    print("2- Pass the monster quietly.")
    answer = input("Enter your response: ")
    if answer == "1":
        diamond_room()
    elif answer == "2":
        game_over("The monster was hungry. He ate you!")
    else:
        game_over("You did not type the number correctly.")


def game_over(reason):
    print("\n" + reason)
    print("Game Over")
    play_again()


def start():
    print("\nYou are standing in a dark room.")
    print("Either take left or right")

    answer = input("Enter your response: ").lower()
    if answer == "l" or "left":
        bear_room()
    elif answer == "r" or "right":
        monster_room()
    else:
        game_over("your response is not appropriate")

start()
