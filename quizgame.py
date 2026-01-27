print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play: )")

answer = input("What does CPU stands for?")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does HTML stand for?")
if answer.lower() == "hypertext markup language":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does URL stand for?")
if answer.lower() == "uniform resource locator":
    print("Correct!")
else:
    print("Incorrect!")
