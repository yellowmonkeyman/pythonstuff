print("This is to demonstrate the use of the remove, reverse, sort, count and extend functions.")

fave_websites = [
    "Reddit.com",
    "Facebook.com",
    "Twitter.com"
]

fave_websites.remove("Facebook.com")
print("{}".format(fave_websites))

fave_websites = [
    "Reddit.com",
    "Facebook.com",
    "Twitter.com"
]

fave_websites.reverse()
print("{}".format(fave_websites))

fave_websites = [
    "Reddit.com",
    "Facebook.com",
    "Twitter.com"
]

fave_websites.sort(reverse = True)
print("Reversed list is {}, {} and {}".format(fave_websites))