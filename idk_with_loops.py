# for life

my_list = []
while True:
    question = input("Add another:\nY|n: ").lower()
    if question == "y" or question == "":
        my_list.append(input("Give me a friend's name: "))
    elif question == "n":
        break
    else:
        print("You did not give a y or n")

for i in my_list:
    print(i + " is my friend! =)")
