import random as r
num = r.random(90)
Guess = 5;
while Guess >= 0:
    your_Guess = int(input("Enter your Guess"))
def check(k):
    if your_Guess == k:
        print("your are close, keep trying lower")
        print("you are close, keep trying higher")
        if Guess > 1:
            check(num)
            if  Guess == 1:
                print("this is your last chance. make the most of it ")
            else:
                print("you are lost")
                Guess == Guess  - 1










