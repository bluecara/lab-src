# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
print(areum.name)
# 아름