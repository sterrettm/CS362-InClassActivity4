def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        raise ValueError("Input is not in domain [0, inf)")

def factorial(n):
    if (n < 0):
        raise ValueError("Input is not in domain [0, inf)")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
