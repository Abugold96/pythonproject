print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play: )")
score = 0

answer = input("What does CPU stands for?")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTML stand for?")
if answer.lower() == "hypertext markup language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does URL stand for?")
if answer.lower() == "uniform resource locator":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")
