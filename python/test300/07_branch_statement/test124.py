# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)
# input number1: 10
# input number2: 9
# input number3: 20
# 20