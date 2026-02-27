# 1. Addition Function
def add(a, b):

    """Returns the sum of a + b."""
    return a + b

# 2. Subtraction Function
def subtract(a, b):

    """Returns the difference of a - b."""
    return a - b

# 3. Multiplication Function
def multiply(a, b):

    """Returns the product of a * b."""
    return a * b

# 4. Division Function
def divide(a, b):

    """Returns the division of a / b. Includes handling for division by zero."""

    if b == 0:

        return "Error: Division by zero is not allowed."

    return a / b
