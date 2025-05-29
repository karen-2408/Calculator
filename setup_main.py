def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error: Cannot take modulus by zero."
    return x % y

def get_operation():
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    
    choice = input("Enter choice (1-6): ")
    if choice in ['1', '2', '3', '4', '5', '6']:
        return choice
    else:
        print("Invalid choice. Please select a valid option.")
        return get_operation()



def main():
    print("Welcome to the Advanced Calculator!")
    
    while True:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        operation = get_operation()
        
        if operation == '1':
            result = add(num1, num2)
        elif operation == '2':
            result = subtract(num1, num2)
        elif operation == '3':
            result = multiply(num1, num2)
        elif operation == '4':
            result = divide(num1, num2)
        elif operation == '5':
            result = power(num1, num2)
        elif operation == '6':
            result = modulus(num1, num2)
        
        print(f"Result: {result}")
        
        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
