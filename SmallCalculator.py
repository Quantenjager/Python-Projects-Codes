print("Write everything in lower case")
print("What do you want to Calculate? add, sub, mul, div, pow")
operation = input()
if operation == "add":
    print("Whats the first number?")
    num1 = int(input())
    print("Whats the second number?")
    num2 = int(input())
    answer=(num1 + num2)
    print(answer)

elif operation == "sub":
    print("Whats the first number?")
    num1 = int(input())
    print("Whats the second number?")
    num2 = int(input())
    answer=(num1 - num2)
    print(answer)

elif operation == "mul":
    print("Whats the first number?")
    num1 = int(input())
    print("Whats the second number?")
    num2 = int(input())
    answer=(num1 * num2)
    print(answer)

elif operation == "div":
    print("Whats the first number?")
    num1 = int(input())
    print("Whats the second number?")
    num2 = int(input())
    answer=(num1 / num2)
    print(answer)

elif operation == "pow":
    print("Whats the first number?")
    num1 = int(input())
    print("Whats the second number?")
    num2 = int(input())
    answer=(num1 ** num2)
    print(answer)