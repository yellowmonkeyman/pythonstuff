titlesequence = "hello world"
print("hello world\n")

print("What data type am I?")
print("You're a string - duh\n")

print("And how many letters are in this sentence?")
print(len("And how many letters are in this sentence?\n"))

print("\nThis is hello world in uppercase using the .upper() method")
print(titlesequence.upper())

print("\n This is hello world in lowercase using the .lower() method")
print(titlesequence.lower())

print("\n This is hello world using the capitalize() method")
print(titlesequence.capitalize())

helloworldcount = titlesequence.count(titlesequence)
print("\n How many times does 'helloworld' fit into 'helloworld'?")

print(helloworldcount)
print("\n At what position is the first 'o' in hello world?")

print(titlesequence.find("o")+1)
print(titlesequence.replace("hello", "goodbye"))



