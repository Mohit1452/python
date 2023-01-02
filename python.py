import random
add = 0
k=1
while k==1:
    roll = int(input("Enter your number: "))
    comp = random.randint(1,6)
    if roll == comp:
        result = "win"
        add += 1
    elif roll != comp:
        result = "lose"



    print("Your number was",roll,"and computer generated number was",comp)
    print("You",result)
    print("Your score is",add)
    k = int(input("Do you want to continue, then enter 1 or else press any other number to exit"))