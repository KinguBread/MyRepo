count = 0
num = int(input("Please give me any number: \n"))
if num < 0:
    print("Your number is negative")
elif num > 0:
    while count < num:
        count = count + 1
        print(count)