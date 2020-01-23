
placearray = [" "," "," "," "," "," "," "," "," "," ","X"," "," "," "," "," "]
# listlength = placearray.count()
# print("The number of tiles is {}".format(listlength))

def render_level1():
    print(" --------- ")
    print("| {} {} {} {} |".format(placearray[0],placearray[1],placearray[2],placearray[3]))
    print("| {} {} {} {} |".format(placearray[4],placearray[5],placearray[6],placearray[7]))
    print("| {} {} {} {} |".format(placearray[8],placearray[9],placearray[10],placearray[11]))
    print("| {} {} {} {} |".format(placearray[12],placearray[13],placearray[14],placearray[15]))
    print(" --------- ")

playerposition = 11

1
1   :

    render_level1()

    value = input("Please 1-4 to move: ")
    print(f'You entered {"value"}')

    #MOVE UP
    if(int(value) == 1):
        print("You pressed 1 to move left\n")
        playerposition = placearray.index("X")
        placearray[playerposition] = " "
        print("{}".format(playerposition))
        if(playerposition > 4):
            newplayerposition = playerposition - 4
            placearray[newplayerposition] = "X"
            #Set the players position to the new position for further calculations
            playerposition = newplayerposition
            render_level1()
        else:
            print("You have reached the top.")

    #MOVE LEFT
    if(int(value) == 2):
        playerposition = placearray.index("X")
        placearray[playerposition] = " "
        if(playerposition == 1 or playerposition == 5 or playerposition == 9 or playerposition == 13):
             print("You have reached the left side.")
        else:
            newplayerposition = playerposition - 1
            placearray[newplayerposition] = "X"
            #Set the players position to the new position for further calculations
            playerposition = newplayerposition
            render_level1()

    #MOVE RIGHT
    if(int(value) == 3):
        playerposition = placearray.index("X")
        placearray[playerposition] = " "
        if(playerposition == 4 or playerposition == 8 or playerposition == 12 or playerposition == 16):
             print("You have reached the right side.")
        else:
            newplayerposition = playerposition + 1
            placearray[newplayerposition] = "X"
            #Set the players position to the new position for further calculations
            playerposition = newplayerposition
            render_level1()
        
    #MOVE DOWN
    if(int(value) == 4):
        playerposition = placearray.index("X")
        placearray[playerposition] = " "
        if(playerposition >= 13):
            print("You have reached the bottom")
        else:
            newplayerposition = playerposition + 4
            placearray[newplayerposition] = "X"
            #Set the players position to the new position for further calculations
            playerposition = newplayerposition
            render_level1()


