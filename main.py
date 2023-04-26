import random
import time

print("Welcome to my geuss the number game")
time.sleep(1)
num = random.randrange(1, 100)

run = True
while run:
    input1 = int(input("guess the number: "))
    if input1 == num:
        print("you win")
        run = False
    elif input1 > num:
        print("the number is lower")
    elif input1 < num:
        print("the number is higher")
    else:
        print("invalid number")