my_list = []
while True:
    my_list.append(input("What is your favorite food? \n"))
    question = input("Do you have another?\nY|n ").lower()
    if question == "y" or question == "":
        my_list.append(input("Please give another one of your favorite foods \n"))
    elif question == "n":
        break
    else:
        print("You did not give a y or n")

for i in my_list:
    print(i + " Is one of your favorite foods!")


