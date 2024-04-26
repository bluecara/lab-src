# 어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생합니다. try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리해보세요.

try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안되요")

# 0으로 나누면 안되요