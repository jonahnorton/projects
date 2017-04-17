health = 100
locations = ["Outside", "Conservatory", "Hallway", "Car"]

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

location_index = 0
print("You pull up outside a modern but dishevelled manor house, knocking on the door yields no results.")
# continue this loop until the player enters the house
while location_index == 0:
    print("You are here:", locations[location_index])
    print("Where do you go first? look for a back door,try a window or get in the car and leave. Which do you choose?")
    print("1: Door")
    print("2: Window")
    print("3: Car")
    outside_action = user_input()
    print

    if outside_action == 1:
        # door is chosen; now in the conservatory
        location_index = 1
        print("The door creaks as you enter revealing a dusty conservatory")
        # continue this loop until player leaves the conservatory
        while location_index == 1:
            print("You are here:", locations[location_index])
            print("You see a door, some shelves and a chest, what would you like to investigate first?")
            print("1: Door")
            print("2: Shelves")
            conservatory_action = user_input()
            print()

            if conservatory_action == 1:
                # go through the door; now in the hallway
                location_index = 2
                print("You enter a dark hallway, you can see nothing but a lightswitch")
                # continue this loop until player leaves the hallway
                while location_index == 2:
                    print("You are here:", locations[location_index])
                    print("What do you do?")
                    print("1: Turn on light switch")
                    print("2: Try to find the your way in the dark")
                    hallway_action = user_input()
                    print()

                    if hallway_action == 1:
                        print("Well you're clever")
                        print("Now that the light is on you go down a stairwell leading to another door and you escape")
                        # escape the house and get in the car
                        location_index = 3
                    elif hallway_action == 2:
                        print("You eventually find the stairs down to the basement but there is somthing on the step, you fall and crack your skull on the stone floor below")
                        print("You are dead")
                        exit()
                    else:
                        print("choose a number")

            elif conservatory_action == 2:
                # still in the conservatory; looking at the shelves
                print("You find a bandage, it will heal 45 health")
                health += 45
                print("Your health is:", str(health))
            else:
                print("choose a number")

    elif outside_action == 2:
        # window is chosen; still outside
        print("The window is locked do you want to try to break it?")
        print("1: Yes")
        print("2: No")
        print()
        WindowAction1 = user_input()
        if WindowAction1 == 1:
            print ("An alarm sounds and lights snap on illuminating the guards who are aboout to shoot you")
        elif WindowAction1 == 2:
            print ("What do you do instead?")
        else:
            print("Choose a number")
    elif outside_action == 3:
        # car is chosen; get in car
        location_index = 3
        print ("That's not a very interesting, is it?")
        print("You are here:", locations[location_index])
    else:
        print("choose a number")

