import random
x = random.randint(1, 100)
c = input("Please press x \n")
if c == "x" or "X":
    print(str(x))
if x <= 50:
    print("Hello")
elif x >= 51:
    print("Goodbye")