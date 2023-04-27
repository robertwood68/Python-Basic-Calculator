from add import add
from sub import sub
from mul import mul
from div import div
from mod import mod
from exit import bye

print("\n\t\t***Enter 'stop' or 'exit' at any point to terminate the program***\t\t\n")

#
# Main function for program
#
def main():
    # draw input from first number
    num1 = input("Please enter your first number:\n")
    if "." in num1:
        num1 = float(num1)
    elif num1.lower() == "stop" or num1.lower() == "exit":
        bye()
    elif any(c.isalpha() for c in num1) or " " in num1 or num1 == "":
        print("That is not a number\n")
        main()
    else:
        num1 = int(num1)
    
    # draw input from second number
    num2 = input("Please enter your second number:\n")
    if "." in num2:
        num2 = float(num2)
    elif num2.lower() == "stop" or num2.lower() == "exit":
        bye()
    elif any(c.isalpha() for c in num2) or " " in num2 or num2 == "":
        print("That is not a number\n")
        main()
    else:
        num2 = int(num2)
    
    # check if function is invalid, otherwise store and execute appropriate function
    func = input("What would you like to do with these numbers? Enter add, subtract, multiply, divide, or mod:\n").lower()
    if func.isdigit():
        print("That is not a function\n")
        main()

    # initialize result variable
    result = 0

    # conditionals for requested functions
    if func == "add" or func == "+":
        result = add(num1, num2)
        print(str(num1) + " + " + str(num2) + " = " + str(result) + "\n")
    elif func == "subtract" or func == "-" or func == "sub":
        result = sub(num1, num2)
        print(str(num1) + " - " + str(num2) + " = " + str(result) + "\n")
    elif func == "multiply" or func == "*" or func == "mult" or func == "mul":
        result = mul(num1, num2)
        print(str(num1) + " * " + str(num2) + " = " + str(result) + "\n")
    elif func == "divide" or func == "/" or func =="div":
        result = div(num1, num2)
        print(str(num1) + " / " + str(num2) + " = " + str(result) + "\n")
    elif func == "mod" or func == "%" or func == "modulus":
        result = mod(num1, num2)
        print(str(num1) + " % " + str(num2) + " = " + str(result) + "\n")
    elif func.lower() == "stop" or func.lower() == "exit":
        bye()
    else:
        print("That is not a valid operation\n")

    # continue if input is yes
    main()

# executes the file, only necessary when a main function is defined in the script
if __name__ == "__main__":
    main()