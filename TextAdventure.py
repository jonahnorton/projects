loop = True
while loop != False:
    print("you pull up outside a modern but dishevelled manor house, knocking on the door yields no results.")
    action1 = int(input("Where do you go first? look for a back door,try a window or get in the car and leave\noption:\n1: Door\n2: Window\n3: Car\n"))
    if action1 ==1:
        print ("The door creaks as you enter revealing a dusty conservatory")
        ConsevatoryAction1 = int(input("You see a door, some shelves and a chest, what would you like to investigate first?\n1: Door\n2: Shelves\n3: chest\n"))
        if ConsevatoryAction1 == 1:
            HallwayAction1 = int(input("you enter a dark hallway, you can see nothing but a lightswich, what do you do?\n1: Turn on light switch\n2: try to find the your way in the dark\n"))
            if HallwayAction1 == 1:
                print ("well your clever")
                HallwayAction2 = input("Now that the light is on you can see a stairwell leading to the basement and second floor, the kitchen")
            elif HallwayAction1 == 2:
                print ("You eventually find the stairs down to the basement but there is somthing on the step, you fall and crack your skull on the stone floor below")
                loop = False
            else:
                print("choose a number")
    elif action1 == 2:
        WindowAction1 = int(input("The window is locked do you want to try to break it?\n1: yes\n2: no\n"))

        if WindowAction1 == 1:
            print ("an alarm sounds and lights snap on illuminating the guards who are aboout to shoot you")
            loop = False
        elif WindowAction1 == 2:
            print ("what do you do instead?")
        else:
            print("choose a number")
    elif action1 == 3:
        print ("That's not a very interesting, is it?")
    else:
        print("choose a number")