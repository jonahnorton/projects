loop = True

while loop != False:
    print("you pull up outside a modern but dishevelled manor house, knocking on the door yields no results.")
    action1 = input("Where do you go first? look for a back door,try a window or get in the car and leave\noption:\n1: Door\n2: Window\n3: Car\n")


    if action1 =="1":
        print ("The door creaks as you enter revealing a dusty conservatory")
        ConsevatoryAction1 = input("You see a door, some shelves and a chest, what would you like to investigate first?\n1: Door\n2: Shelves\n3: chest\n")


    elif action1 == "2":
        print ("The window is locked do you want to try to break it?")
        WindowAction1 = input("y/n\n")
        if WindowAction1 == "y":
            print ("an alarm sounds and lights snap on illuminating the guards who are aboout to shoot you")
            loop = False
        elif WindowAction1 == "n":


    elif action1 == "3":
        print ("That's a bit of a boring choice is'nt it? are you sure?")


    else:
        print ("choose a number between 1 and 3")