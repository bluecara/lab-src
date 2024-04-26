# 다음과 같은 코드 구조를 사용하면 예외 발생 시 에러 메시지를 변수로 바인딩할 수 있습니다.
'''
try:
    실행코드
except 예외 as 변수:
    예외처리코드

'''

# 리스트의 인덱싱에 대해 에러를 출력해보세요.
'''
data = [1, 2, 3]

for i in range(5)
    print(data[i])

'''

data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

'''
1
2
3
list index out of range
list index out of range
'''