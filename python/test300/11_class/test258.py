# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("불명", "미상", "모름")
areum.who()      # Human.who(areum)
# 이름: 불명 나이: 미상 성별: 모름

areum.setInfo("아름", 25, "여자")
areum.who()      # Human.who(areum)
# 이름: 아름 나이: 25 성별: 여자