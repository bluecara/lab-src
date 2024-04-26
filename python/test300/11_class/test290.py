# 다음 코드의 실행 결과를 예상해보세요.

class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()
# 자식생성
# 부모생성