HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No History found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print("History cleared.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")   # "8 + 2" "=" "10"
    file.close()

def calculate(user_input):

    parts = user_input.split() # split user input...
    if len(parts) != 3:
        print("Invalid Input..Use format -> Num Operator Num (eg. 8 + 8)")
        return
    
    num1 = float(parts[0])  # Access the first split part of user input (eg. 8+2 => accessing 8 and convert into float)
    op = parts[1]
    num2 = float(parts[2])  # Access the third split part of user input (eg. 8+2 => accessing 2 and convert into float)

#  >> check for operation
    if op == "+":
        result =  num1 + num2
    elif op == "-":
        result =  num1 - num2
    elif op == "*":
        result =  num1 * num2
    elif op == "/":
        if num2 == 0:
            result = "Error(Division by Zero)"
            print("Can not divisible by Zero.")
            save_to_history(user_input, result)
            return
        result = num1 / num2

    elif op == "%":
        if num2 == 0:
            result = "Error (Modulus by Zero)"
            print("Can't take Modulus With Zero.")
            save_to_history(user_input, result)
            return
        result = num1 % num2
    
    elif op == "^" or op == "**":
        result = num1 ** num2

    else:
        print("Invalid Operator!")
        return
        
    if int(result) == result:
        result = int(result)
    print("Result:",result)
    save_to_history(user_input, result)

def main():
    print(">> BASIC CALCULATOR <<")
    while True:
        user_input = input("Enter Expression OR Command (history, clear, exit) :")
        if user_input == 'exit':
            print("Good Bye!")
            break

        elif user_input == 'clear':
            clear_history()

        elif user_input == 'history':
            show_history()
        else:
            calculate(user_input)   

main()  # calling main function

    
