import random

def game():
    print("You are playing game")
    score = random.randint(1,62)
    # fetch the hiscore
    with open("highscore.txt") as f:
        hiscore = (f.read())
        if(hiscore !=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    
    print(f"Your score is {score}")
    if(score > hiscore):
        with open("highscore.txt", "w") as f:
            f.write(str(score))

game()