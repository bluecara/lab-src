# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.

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

    def 정보(self):
        super().정보()
        print("구동계 ", self.구동계)

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

# 바퀴수  2
# 가격  100
# 구동계  시마노