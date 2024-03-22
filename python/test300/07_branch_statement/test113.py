# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.

user = input("입력: ")
if int(user) % 2 == 0:
    print("짝수")
else:
    print("홀수")
# 입력: 5
# 홀수