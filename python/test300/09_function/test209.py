# 아래 코드의 실행 결과를 예측하라.

def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

'''
B
A
'''