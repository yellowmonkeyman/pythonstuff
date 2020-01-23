fave_websites = [
    "Reddit.com",
    "Facebook.com",
    "Twitter.com"
]

print("\nMy favourite websites are {}, {} and {}\n".format(fave_websites[0], fave_websites[1], fave_websites[2]))

fave_websites.append("Dailymail.com")
fave_websites.append("w3schools.com")

print("APPENDED - two more websites added")
print("\nMy favourite websites are {}, {}, {}, {} and {}\n".format(fave_websites[0], fave_websites[1], fave_websites[2], fave_websites[3], fave_websites[4]))

fave_websites.pop();

print("POP - the last website was removed using pop")
print("\nMy favourite websites are {}, {}, {}, and {}\n".format(fave_websites[0], fave_websites[1], fave_websites[2], fave_websites[3]))