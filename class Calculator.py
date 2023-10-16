class Calculator:

    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def add(self):
        return self.operand1 + self.operand2

    def subtract(self):
        return self.operand1 - self.operand2

    def multiply(self):
        return self.operand1 * self.operand2

    def divide(self):
        if self.operand2 == 0:
            return "Error: Division by zero"
        return self.operand1 / self.operand2

# Input from the user
expression = input("Enter an expression (e.g., '2+3'): ")

# Try to split the expression into operator and operands
try:
    operator = expression[1]
    operand1 = float(expression[0])
    operand2 = float(expression[2])

    # Create a calculator object
    calculator = Calculator(operand1, operand2)

    # Call the appropriate function based on the operator
    if operator == '+':
        result = calculator.add()
    elif operator == '-':
        result = calculator.subtract()
    elif operator == '*':
        result = calculator.multiply()
    elif operator == '/':
        result = calculator.divide()
    else:
        result = "Error: Invalid operator"

    # Display the result
    print("Result:", result)

except (ValueError, IndexError):
    print("Error: Invalid expression format")
