print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay let's play: )")

answer = input("What does CPU stands for?")
if answer == "central processing unit":
    print("Correct!")
