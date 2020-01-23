word = "Classic"
print("Word length = " + str(len(word)))
print("First letter: " + word[0])
print("Last letter: " + word[6])

if(word[0].lower() == word[len(word)].lower()):
    print("Last letter is same as the first")
    
else:
    print("First and last letter do not match")
    