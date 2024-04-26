# 다음 코드가 동작하도록 차 클래스를 수정하세요.

class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

# 바퀴수  2
# 가격  100