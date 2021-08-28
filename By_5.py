import time
num = int(input("Please give me a number: \n"))
count = 0
while count < num:
    count = count + 5
    print(count)
    time.sleep(0.5)
print("Goodbye!")