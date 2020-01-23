import random

random_list = []

for i in range(5):
    i = random.randint(0, 50)
    random_list.append(i)
    print("New random number = " + str(i))

print(random_list)
