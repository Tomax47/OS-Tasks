#!/usr/bin/python3

import sys
import random
import time

def generate_expression():
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y
    elif operator == '/':
        if y == 0:
            result = "undefined"
        else:
            result = round(x / y, 2)

    return f"{x} {operator} {y} = {result}"

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if not (120 <= n <= 180):
            raise ValueError
    except ValueError:
        sys.exit(1)

    for _ in range(n):
        expression = generate_expression()
        print(expression)
        time.sleep(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
