# FizzBuzz
import sys

x = sys.stdin.readline().rstrip()
y = sys.stdin.readline().rstrip()
z = sys.stdin.readline().rstrip()

def check(n):
    if n[0] == 'F' and len(n) == 4:
        return "3O5X"
    elif n[0] == 'F' and len(n) == 8:
        return "3O5O"
    elif n[0] == 'B':
        return "3X5O"
    else:
        return int(n)

def number(n, m):
    if n == 'x' and type(m) is int:
        return m + 3
    elif n == 'y' and type(m) is int:
        return m + 2
    elif n == 'z' and type(m) is int:
        return m + 1
    else:
        return 0

result = max(number('x', check(x)), number('y', check(y)), number('z', check(z)))

if result % 3 == 0:
    if result % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif result % 5 == 0:
    print("Buzz")
else:
    print(result)
