# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.

class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        #차.__init__(self, 바퀴, 가격)
        self.구동계 = 구동계


bicycle = 자전차(2, 100, "시마노")
print(bicycle.구동계)
# 시마노
print(bicycle.바퀴)
# 2