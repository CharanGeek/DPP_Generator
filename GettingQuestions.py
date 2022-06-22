import random

def GetQuestions(sub,quesNum):
    # Getting the questions inside a variable as a list
    with open(sub,"r") as f:
        unfilteredQuestion =  f.readlines()


    # Removing new line escape sequence from the list
    filteredQuestions = []
    for items in unfilteredQuestion:
        if items[0:-1] == '':
            continue

        filteredQuestions.append(items[0:-1])

    # Generating 10 random unique numbers
    def generateRandNum():
        endIndex = len(filteredQuestions) - 1
        allRandNum = random.sample(range(0,endIndex),quesNum)
        return allRandNum

    allRandNum = []
    finalQuestions = []

    # Appending random 10 questions inside finalQuestion list
    for items in generateRandNum():
        finalQuestions.append(filteredQuestions[items])

    return finalQuestions
