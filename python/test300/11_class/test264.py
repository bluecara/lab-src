# 객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

a = Stock(None, None)
a.set_code("005930")
print(a.code)
# 005930