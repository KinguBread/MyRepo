#num = int(input("Give me a number: \n")
#print(num)

while True:
    try:
        num = int(input("Give me a number: \n"))
        break
    except:
        print("You did not enter a number")
        continue
print(num)

