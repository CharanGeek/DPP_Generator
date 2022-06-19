import random

def GetQuestions():
    # Getting the questions inside a variable as a list
    with open("Question Bank","r") as f:
        unfilterQuestion =  f.readlines()


    # Removing new line escape sequence from the list
    filterQuestions = []
    for items in unfilterQuestion:
        if items[0:-1] == '':
            continue

        filterQuestions.append(items[0:-1])

    # Generating 10 random unique numbers
    def generateRandNum():
        endIndex = len(filterQuestions) - 1
        allRandNum = random.sample(range(0,endIndex),10)
        return allRandNum

    allRandNum = []
    finalQuestions = []

    # Appending random 10 questions inside finalQuestion list
    for items in generateRandNum():
        finalQuestions.append(filterQuestions[items])

    return finalQuestions
