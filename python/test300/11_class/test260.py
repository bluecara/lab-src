# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.

class OMG :
    def print() :
        print("Oh my god")


mystock = OMG()
mystock.print()      # OMG.print(mystock)

'''
Traceback (most recent call last):
  File "test260.py", line 9, in <module>
    mystock.print()      # OMG.print(mystock)
    ^^^^^^^^^^^^^^^
TypeError: OMG.print() takes 0 positional arguments but 1 was given
'''