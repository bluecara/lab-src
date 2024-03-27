# 아래의 에러가 발생하는 이유에 대해 설명하라.

hello()
def hello():
    print("Hi")
'''
Traceback (most recent call last):
  File "test205.py", line 3, in <module>
    hello()
    ^^^^^
NameError: name 'hello' is not defined. Did you mean: 'help'?
'''

# 함수가 정의되기 전에 호출되어서 에러가 발생합니다.
