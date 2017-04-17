#health = 100
locations = ["Outside", "Conservatory", "Hallway"]
location_index = 0
selection = True
#alive = True

def user_input():
    # test user input using try... except
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            selection = int(input("Please enter your selection: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue
        else:
            #age was successfully parsed!
            #we're ready to exit the loop.
            break
    return selection

print("you pull up outside a modern but dishevelled manor house, knocking on the door yields no results.")
print("Where do you go first? look for a back door,try a window or get in the car and leave\noption:\n1: Door\n2: Window\n3: Car\n")
action1 = user_input()
location = locations[location_index]
if action1 == 1:
    location_index = 1
    print("The door creaks as you enter revealing a dusty conservatory")
    print("you are here:", locations[location_index])
    print("You see a door, some shelves and a chest, what would you like to investigate first?\n1: Door\n2: Shelves\n")
    ConsevatoryAction1 = user_input()
    while location_index == 1:
        if ConsevatoryAction1 == 1:
            location_index = 2
            print("you enter a dark hallway, you can see nothing but a lightswich, what do you do?\n1: Turn on light switch\n2: try to find the your way in the dark\n")
            print("you are here:", locations[location_index])
            HallwayAction1 = None
            while location_index == 2:
                if HallwayAction1 == None:
                    HallwayAction1 = user_input()
                if HallwayAction1 == 1:
                    print ("well your clever")
                    print("Now that the light is on you can see a stairwell leading to the basement and second floor, the kitchen")
                    location_index == 3
                    HallwayAction1 = None
                    #TODO: add an action here
                elif HallwayAction1 == 2:
                    print ("You eventually find the stairs down to the basement but there is somthing on the step, you fall and crack your skull on the stone floor below")
                    HallwayAction1 = None
                else:
                    print("choose a number")
                    HallwayAction1 = None
        elif ConsevatoryAction1 == 2:
            print("you find a bandage, it will heal 45 health")
        else:
            print("choose a number")
elif action1 == 2:
    print("The window is locked do you want to try to break it?\n1: yes\n2: no\n")
    WindowAction1 = user_input()

    if WindowAction1 == 1:
        print ("an alarm sounds and lights snap on illuminating the guards who are aboout to shoot you")
        #health += -100

    elif WindowAction1 == 2:
        print ("what do you do instead?")
    else:
        print("choose a number")
elif action1 == 3:
    print ("That's not a very interesting, is it?")
else:
    print("choose a number")