# 후위 표기식
# 스택
from string import ascii_uppercase
import sys

input = sys.stdin.readline

X = input().rstrip()

alphabet = list(ascii_uppercase)
stack = []

result = ""

for x in X:
    if x in alphabet:
        result += x # 피연산자는 바로 결과에 추가
    elif x == '(':
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(': # 닫는 괄호는 여는 괄호를 만날 때까지 pop
            result += stack.pop()
        stack.pop() # '(' 삭제
    elif x == '*' or x == '/':
        while stack and stack[-1] in ('*', '/'): # 곱셈 / 나눗셈은 같은 우선순위인 *, /만 pop
            result += stack.pop()
        stack.append(x)
    elif x == '+' or x == '-':
        while stack and stack[-1] != '(': # 덧셈 / 뺄셈은 자신보다 우선순위가 높거나 같은 것(+, -, *, /) 모두 pop
            result += stack.pop()
        stack.append(x)

while stack:
    result += stack.pop()

print(result)
