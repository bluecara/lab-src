# 아래와 같은 에러가 발생하는 원인을 설명하라.

def 함수(a, b) :
    print(a + b)

함수("안녕", 3)
'''
Traceback (most recent call last):
  File "test214.py", line 6, in <module>
    함수("안녕", 3)
  File "test214.py", line 4, in 함수
    print(a + b)
          ~~^~~
TypeError: can only concatenate str (not "int") to str
'''

# 정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 적용하려는 의도로 설계됐습니다. 하지만 함수를 호출 할때 문자열과 숫자를 입력해서 문자열과 숫자는 더할 수 없다는 에러가 발생합니다.
