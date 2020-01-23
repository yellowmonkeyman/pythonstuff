num = 106

#Extended slice = [start, stop, step].
#There is no start, no stop but -1 indicates to start at the end and stop at the start.

if(str(num) == str(num)[::-1]):
    print("This is a palindrome")
else:
    print("This is not a palindrome")