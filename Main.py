from MakingPDF import MakePdf
line = "---------------------------------------------------------------"

def Menu():
    print("Welcome to the DPP Generator!")
    print("Which subject's DPP do you want to generate?")
    print("Example -> If you type 2 then Physics DPP will be generated")
    print("1) Maths")
    print("2) Physics")
    print("3) Chemistry")
    print("4) Biology")
    print("5) English")
    print("6) Hindi")
    print("7) Geography")
    print("8) History")
    print("9) All Subjects Combined")
    print(line)
    choice = input("Enter your choice (default = 9): ")
    
    menu = {
        1 : "Question Bank/Maths.txt",
        2 : "Question Bank/Physics.txt",
        3 : "Question Bank/Chemistry.txt",
        4 : "Question Bank/Bio.txt",
        5 : "Question Bank/English.txt",
        6 : "Question Bank/Hindi.txt",
        7 : "Question Bank/Geography.txt",
        8 : "Question Bank/History.txt",
        9 : "Question Bank/Combined.txt",
    }

    if choice == '':
        choice = 9
    sub = menu.get(int(choice))

    noOfQuestions = input("Enter the number of questions you want to get (default = 10): ")
    
    if noOfQuestions == '':
        noOfQuestions = 10

    return sub, int(noOfQuestions)


def Bye():
    print(line)
    print("Thank you for using this script!")
    print("Made by Aditya Tiwari")
    print("Follow me on:")
    print("\tInstagram: uncanny_adi")
    print("\tInstagram: aditya_tivarii")
    print("\tDiscord: aawditya #1366")
    print(line)

sub, noOfQuestions = Menu()
MakePdf(sub,noOfQuestions)
Bye()