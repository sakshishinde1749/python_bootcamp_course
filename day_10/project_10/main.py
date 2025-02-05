from ascii_logo import calculator_logo

print(calculator_logo)

def calculator(first_num, operator, second_num):
    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == '*':
        result = first_num * second_num
    elif operator == '/':
        if second_num == 0:
            return "Error: Division by zero is not allowed"
        result = first_num / second_num
    else:
        return "Error operator is not valid"
    
    return round(result, 2)
    

while True:
    if 'final_result' not in locals() or response == 'n':
        first_num_input = float(input("What\'s the first number?: "))
    elif response == 'y':
        first_num_input = final_result

    print("\n+\n-\n*\n/\n")
    operator_input = input("Pick an operator: ")

    second_num_input = float(input("\nWhat\'s the second number?: "))

    final_result = calculator(first_num_input, operator_input, second_num_input)

    print(f"{first_num_input} {operator_input} {second_num_input} : {final_result}")

    response = input(f"Type 'y' to continue calculating with {final_result}, or 'n' to start a new calculation: ").lower()




