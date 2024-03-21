# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.

'''
>> t = (1, 2, 3)
>> t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment

'''

print("tuple은 원소(element)의 값을 변경할 수 없습니다.")