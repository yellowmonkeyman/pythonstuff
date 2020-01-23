
import time

space1 = " "
space2 = " "
space3 = " "
space4 = " "
space5 = " "
space6 = " "
space7 = " "
space8 = " "
space9 = " "

gonumber = 0

print("INSTRUCTIONS\n")
print("\nUse the number keys to select the quadrant you wish to make your move to.\n")
print("\nIs that understood?\n")
print("\nY / N")


def print_grid():
    print("\n   |   |   ")
    print(" {} | {} | {} ".format(space1, space2, space3))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {} | {} | {} ".format(space4, space5, space6))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {} | {} | {} ".format(space7, space8, space9))
    print("   |   |   \n")

print_grid()

def thankstext():
    print(r"     _   _                 _                       ")
    print(r"    | | | |               | |                      ")
    print(r"    | |_| |__   __ _ _ __ | | ___   _  ___  _   _  ")
    print(r"    | __| '_ \ / _` | '_ \| |/ / | | |/ _ \| | | | ") 
    print(r"    | |_| | | | (_| | | | |   <| |_| | (_) | |_| | ")
    print(r"     \__|_| |_|\__,_|_| |_|_|\_\\__, |\___/ \__,_| ")
    print(r"                                 __/ |             ")
    print(r"                                |___/              ")

def winconditions():

    #horizontals
    if (space1 == "X" and space2 == "X" and space3 == "X"):
        print("Player " + space1 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()
        
    if(space1 == "O" and space2=="O" and space3 == "O"):
        print("Player " + space1 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if (space4 == "X" and space5 == "X" and space6 == "X"):
        print("Player " + space4 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if(space4 == "O" and space5=="O" and space6 == "O"):
        print("Player " + space4 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if (space7 == "X" and space8 == "X" and space9 == "X"):
        print("Player " + space7 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if(space7 == "O" and space8=="O" and space9 == "O"):
        print("Player " + space7 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    #Verticals
    if (space1 == "X" and space4 == "X" and space7 == "X"):
        print("Player " + space1 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if(space1 == "O" and space4=="O" and space7 == "O"):
        print("Player " + space1 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if (space2 == "X" and space5 == "X" and space8 == "X"):
        print("Player " + space2 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if(space2 == "O" and space5=="O" and space8 == "O"):
        print("Player " + space2 + " has won!")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if (space3 == "X" and space6 == "X" and space9 == "X"):
        print("Player " + space3 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if(space3 == "O" and space8=="O" and space9 == "O"):
        print("Player " + space3 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    #Diagonals
    if (space1 == "X" and space5 == "X" and space9 == "X"):
        print("Player " + space1 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if(space1 == "O" and space5=="O" and space9 == "O"):
        print("Player " + space1 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if (space3 == "X" and space5 == "X" and space7 == "X"):
        print("Player " + space3 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

    if(space3 == "O" and space5=="O" and space7 == "O"):
        print("Player " + space3 + " has won!\n")
        time.sleep(1)
        thankstext()
        print("Exiting..\n")
        time.sleep(2)
        exit()

while (gonumber < 9):
    if(gonumber == 0):

        space1 = "1"
        space2 = "2"
        space3 = "3"
        space4 = "4"
        space5 = "5"
        space6 = "6"
        space7 = "7"
        space8 = "8"
        space9 = "9"

        print_grid()
        print("INSTRUCTIONS\n")
        print("\nUse the number keys to select the quadrant you wish to make your move to.\n")

        space1 = " "
        space2 = " "
        space3 = " "
        space4 = " "
        space5 = " "
        space6 = " "
        space7 = " "
        space8 = " "
        space9 = " "

    value = input("Please enter a number 1-9 corresponding to the tictactoe segment (top left to bottom right): ")
    print(f'You entered {value}')


    if gonumber % 2 == 0:

        if int(value) == 1:
            space1 = "X"
            print_grid()
            gonumber += 1

        if int(value) == 2:
            space2 = "X"
            print_grid()
            gonumber += 1

        if int(value) == 3:
            space3 = "X"
            print_grid()
            gonumber += 1

        if int(value) == 4:
            space4 = "X"
            print_grid()
            gonumber += 1

        if int(value) == 5:
            space5 = "X"
            print_grid()
            gonumber += 1

        if int(value) == 6:
            space6 = "X"
            print_grid()
            gonumber += 1

        if int(value) == 7:
            space7 = "X"
            print_grid()
            gonumber += 1

        if int(value) == 8:
            space8 = "X"
            print_grid()
            gonumber += 1

        if int(value) == 9:
            space9 = "X"
            print_grid() 
            gonumber += 1   
    
    else:

        if int(value) == 1:
            space1 = "O"
            print_grid()
            gonumber += 1

        if int(value) == 2:
            space2 = "O"
            print_grid()
            gonumber += 1

        if int(value) == 3:
            space3 = "O"
            print_grid()
            gonumber += 1

        if int(value) == 4:
            space4 = "O"
            print_grid()
            gonumber += 1

        if int(value) == 5:
            space5 = "O"
            print_grid()
            gonumber += 1

        if int(value) == 6:
            space6 = "O"
            print_grid()
            gonumber += 1

        if int(value) == 7:
            space7 = "O"
            print_grid()
            gonumber += 1

        if int(value) == 8:
            space8 = "O"
            print_grid()
            gonumber += 1

        if int(value) == 9:
            space9 = "O"
            print_grid() 
            gonumber += 1

    winconditions()



    
    



