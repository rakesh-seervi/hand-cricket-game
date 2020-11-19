import random

you = None
ran = 0
totalruns = 0

while you != ran:
    you = input("Enter the runs from 1 to 10: ")
    if int(you)>10 :
        print(f"you have entered the number {you} please enter number between 1 to 10 ")
        continue 
    ran = random.randint(1, 10)       
    userList = you.split()
    for num in userList:
        totalruns += int(num)
    
    print(f"your run : {you}")
    print(f"computer choose: {ran}")
    
    if int(you) == ran :
        print("you are out")
        break
            
print("totalruns =", totalruns)

with open("highscore.txt", "r") as f:
    highscore = int(f.read())

if(totalruns>highscore):
    print("You have just broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(totalruns))
