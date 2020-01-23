space1 = "X"
space2 = "X"
space3 = "X"
space4 = " "
space5 = " "
space6 = " "
space7 = " "
space8 = " "
space9 = " "

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

if (space1 == "X" and space2 == "X" and space3 == "X"):
        print("Player " + space1 + "has won!")

if(space1 == "O" and space2=="O" and space3 == "O"):
        print("Player " + space1 + "has won!")