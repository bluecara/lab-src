# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.

class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)


car = 자동차(4, 1000)
car.정보()
# 바퀴수  4
# 가격  1000