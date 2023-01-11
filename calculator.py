import PySimpleGui as sg
print("||Calculator MK5 by Alvin Fung||")

sg.Window(title="Hellow World", layout=[[]], margins=(100, 50)).read()

while True:

    num1 = float(input("Please enter the first number: "))
    op = str(input("Please enter an operation to use: "))
    while True:

        if op == "*" or op == "/" or op == "+" or op == "-":
            break
        else:
            print("Please enter an appropriate operator! ")
            op = str(input("Please enter an operation to use: "))
            continue

    num2 = float(input("Please enter the second number: "))

    if op == "*":
        print("Your answer is: ", num1 * num2)

    elif op == "/":
        print("Your answer is: ", num1 / num2)

    elif op == "+":
        print("Your answer is: ", num1 + num2)

    elif op == "-":
        print("Your answer is: ", num1 - num2)

    else:
        print("Invalid operator! Please try again")
        continue

    again = input("Would you like perform another operation? ")
    if again == "Yes" or again == "yes":
        continue
    elif again == "No" or again == "no":
        break
