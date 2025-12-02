Task: Small calculator using a class. Supports Addition, Subtraction, Multiplication, Division.
Handle division-by-zero safely.

Problem-1 -- Solution :


class Calculator:
    def __init__(self, a: float, b: float):
        self.a = float(a)
        self.b = float(b)

    def add(self) -> float:
        return self.a + self.b

    def subtract(self) -> float:
        return self.a - self.b

    def multiply(self) -> float:
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b

def calculate(a, b, operation: str):
    op = operation.strip().lower()
    calc = Calculator(a, b)
    if op in ("add", "+", "addition"):
        return calc.add()
    if op in ("subtract", "-", "sub"):
        return calc.subtract()
    if op in ("multiply", "*", "mul"):
        return calc.multiply()
    if op in ("divide", "/"):
        return calc.divide()
    return f"Error: Unknown operation '{operation}'. Supported: add, subtract, multiply, divide"

# Example usage when running this file directly
if __name__ == "__main__":
    # You may change these sample inputs to test quickly
    samples = [
        (10, 2, "add"),
        (10, 2, "subtract"),
        (10, 2, "multiply"),
        (10, 0, "divide"),
        (10, 2, "divide"),
        (5, 3, "unknown")
    ]
    for a, b, op in samples:
        print(f"{a} {op} {b} -> {calculate(a, b, op)}")


Explanation:

Calculator encapsulates operations.
calculate() is a wrapper that accepts operation strings and returns results or friendly errors.

Complexity: O(1) time & O(1) space.



