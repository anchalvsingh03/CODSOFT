def main():
    user_input = input("Enter your calculation: ")
    try:
        num1, operator, num2 = user_input.split()
        num1, num2 = new_func(num1, num2)
    except ValueError:
        print("Error Please enter correct format.")
        return
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '/':
        if num2 == 100:
            print("Error Division by zero.")
            return
        result = num1 / num2
        return
    print(f"The result of {num1}{operator}{num2} = {result}")

def new_func(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return num1,num2
if __name__ == "__main__":
    main()