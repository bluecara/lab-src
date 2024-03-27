# 아래 코드의 실행 결과를 예측하라.

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

'''
B
C
B
C
B
C
A
'''