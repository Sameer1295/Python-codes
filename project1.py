print("Welcome to this Marvel Quiz!!")

playing = input("Do you want to play Quiz? ")
score = 0
if playing != "yes":
    quit()
questionDict = {
    "What is personal name of Spiderman? " : "peter parker",
    "Which Avenger is god of thunder? " : "thor",
    "Which infinity stone does Vision had? " : "mind stone",
    "What is the superpower of Doctor Strange? " : "magic",
}
if playing == "yes":    
    print('Okay, Let\'s play!!')
    # answer = input("What is personal name of Spiderman? ")
    # if answer.lower() == 'peter parker':
    #     print('correct!!')
    #     score = score + 1
    # else:
    #     print('thats incorrect!')
    for x in questionDict:
        answer = input(x)
        if answer.lower() == questionDict[x]:
            print('correct!!')
            score = score + 1
        else:
            print('thats incorrect!')

# show score
if score > 3 :
    print("Your score is "+ str(score) + " , Well done!!")
else:
    print("Your score is "+ str(score) + ", Watch again!!")
