def multiplication(a,b):
    """Returns the product of a and b."""
    return a * b
def division(a,b):
    """Returns the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b