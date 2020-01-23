num = 11

if(num % 3 == 0 and num % 5 == 0):
    print("Fizzbuzz")
elif(num % 3 == 0):
    print("fizz")
elif(num % 5 == 0):
    print("buzz")
else:
    print("" + str(num))