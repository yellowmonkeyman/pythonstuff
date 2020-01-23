fave_films = ["Die Hard", "Fellowship of the Ring", "Ghostbusters", "Return of the King", "Harry Potter"]
fave_films.append("Fifth Element")
fave_films.append("Butterfly effect")

for i in range(len(fave_films)):
    print(fave_films[i])

def film_check():
    if (fave_films[2] == "Ghostbusters"):
        print("Yey it's Ghostbusters!")
    else:
        print("Booo, we want Ghostbusters!")

film_check()