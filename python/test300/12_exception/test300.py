# 파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.
'''
try:
    실행 코드
except:
    예외가 발생했을 때 수행할 코드
else:
    예외가 발생하지 않았을 때 수행할 코드
finally:
    예외 발생 여부와 상관없이 항상 수행할 코드

'''

# 아래의 코드에 대해서 예외처리를 사용하고 try, except, else, finally에 적당한 코드를 작성해봅시다. else와 finally는 적당한 문구를 print하시면 됩니다.
'''
per = ["10.31", "", "8.00"]

for i in per:
    print(float(per))

'''

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")

'''
10.31
clean data
변환 완료
0
변환 완료
8.0
clean data
변환 완료
'''