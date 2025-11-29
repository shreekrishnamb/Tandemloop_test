class Calculator:
    def compute(self, a, b, operation):
        op = operation.lower()
        
        if op in ["addition", "+"]:
            return a + b
        elif op in ["subtraction", "-"]:
            return a - b
        elif op in ["multiplication", "*"]:
            return a * b
        elif op in ["division", "/"]:
            if b == 0:
                return "Error: Cannot divide by zero."
            return a / b
        else:
            return "Error: Invalid operation type."



if __name__ == "__main__":
   
    my_calc = Calculator()

    print("Simple Calculator")

    try:
        # 1. Input
        a = float(input("Enter value for 'a' (double): "))
        b = float(input("Enter value for 'b' (double): "))
        
        print("\nChoose operation: Addition, Subtraction, Multiplication, Division")
        op_type = input("Enter type of operation: ")

        # 2. Perform Operation
        result = my_calc.compute(a, b, op_type)

        # 3. Output
        print("-" * 20)
        print(f"Result: {result}")
        print("-" * 20)

    except ValueError:
       
        print("\nError: Please enter valid numbers for 'a' and 'b'.")