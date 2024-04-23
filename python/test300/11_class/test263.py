# 객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자")  # Stock.set_name(a, "삼성전자")
print(a.name)
# 삼성전자