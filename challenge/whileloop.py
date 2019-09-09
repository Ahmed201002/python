import random
highest=10
guess=0
answer=random.randint(1,highest)
print("please guess a number between 1 and {}".format(highest))
while guess!=answer:
    guess=int(input())
    if guess>answer:
        print("pls guess a lower value")
    elif guess<answer:
        print("pls a higher value ")
    else:
        print("well done you suggested it")
