# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

삼성 = Stock("삼성전자", "005930")
print(삼성.name)
# 삼성전자
print(삼성.code)
# 005930
print(삼성.get_name())
# 삼성전자
print(삼성.get_code())
# 005930