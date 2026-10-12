history_file = "history.txt"

def show_histiry():
    file = open(history_file,'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(history_file,'w') 
    file.close()
    print("History cleared.") 

def save_history(equation,result):
    file = open(history_file,'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
       print("Invalid input.Use format: number operator (e.g 8 + 8 )")
       return
    

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1+num2
    elif op == "-":
        result = num1-num2
    elif op == "*":
        result = num1*num2 
    elif op == "/":
        if num2 == 0:
            print("Cant divide by zero")
            return
        result  = num1 / num2
    else:
        print('Invlalid operator.use only + - * /')
        return 
    if int(result) == result:
        result = int(result) 
    print("Result: ",result)    
    save_history(user_input,result)

def main():
    print("--SIMPLE CALCULATOR (type history,clear or exit)")
    while True:
        user_input = input("ENter Calculation (+ - * /) or command (history,clear ,exit): ")
        if user_input == "exit":
            print("GoodBye")
            break
        elif user_input == "history":
            show_histiry()
        elif user_input == "clear":
               clear_history()
        else:
            calculator(user_input)      

main()