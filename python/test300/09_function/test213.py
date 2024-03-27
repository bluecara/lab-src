# 아래와 같은 에러가 발생하는 원인을 설명하라.

def 함수(문자열) :
    print(문자열)
함수()
'''
Traceback (most recent call last):
  File "test213.py", line 5, in <module>
    함수()
TypeError: 함수() missing 1 required positional argument: '문자열'
'''

# 함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다.
