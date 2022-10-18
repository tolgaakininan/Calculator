import os
logo = """
 _____________________
|  _________________  |
| | TAIIMF        0.| |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(a,b):
    return a+b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    
    calc=True
    continueCalc=False
    while calc:
        print(logo)
        num1=int(input("What's the first number: "))
        print("/ * - +")
        operation=input("Pick an operation: ")
        num2=int(input("What's the other number: "))
        answer=operations[operation](num1,num2)
        print(f"{num1}{operation}{num2}={answer}")
        contCalc=input(f"Type 'y' to calculating with {answer}, or type 'n' to start new calculation if you want to quit type 'q': ")
        if contCalc=='y':
            continueCalc=True
        elif contCalc=='n':
            continueCalc=False
        elif contCalc=='q':
            calc=False
        while continueCalc:
            operation=input("Pick an operation: ")
            num1=answer
            num2=int(input("What's the number? "))
            answer=operations[operation](num1,num2)
            print(f"{num1}{operation}{num2}={answer}")  
            contCalc=input(f"Type 'y' to calculating with {answer}, or type 'n' to start new calculation if you want to quit type 'q': ")
            if contCalc=='y':
                continueCalc=True
            elif contCalc=='n':
                continueCalc=False
                os.system("cls")
            elif contCalc=='q':
                calc=False

calculator()
os.system("cls")
print("TAKE CARE!")
