# Proportion Tools by cscheerer on GitHub #

import math

def proportionSolver():
    
    print("Please use proportions with one missing variable (x)")
    print("")
    userInput = input("Enter first two diagnal numbers with a space inbetween. > ")
    crossProd = userInput.split()
    
    crossProd1 = int(crossProd[0])
    crossProd2 = int(crossProd[1])
    
    userInput = input("Enter number diagnal to x. > ")
    diviend = int(userInput)
    
    preAnswer = crossProd1 * crossProd2
    Answer = preAnswer / diviend
    Answer = int(Answer)
    
    print(f"The missing variable is: {Answer}")
def proportionChecker():
    print("Please enter the first two diagnal numbers in the proportion.")
    userInput = input("First > ")
    firstNumber = userInput
    userInput = input("Second > ")
    secondNumber = userInput
    
    print("Enter next numbers.")
    userInput = input("Third > ")
    thirdNumber = userInput
    userInput = input("Fourth > ")
    fourthNumber = userInput
    
    try:
        firstSet = int(firstNumber) * int(secondNumber)
        secondSet = int(thirdNumber) * int(fourthNumber)
        
        if firstSet == secondSet:
            print("Proportions Equal.")
        else:
            print("Proportions Inequal")
    
    except:
        print("BAD CODE YOU ZERO RIZZ LOW LIFE LOSER")

print("Welcome. Please choose an option.")
print("[1] Solve Proportion")
print("[2] Check Proportion")
print("")
userInput = input("> ")

if userInput == "1":
    proportionSolver()
elif userInput == "2":
    proportionChecker()
else:
    print("Invalid input.")

