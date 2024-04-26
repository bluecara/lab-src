# 다음 코드의 실행 결과를 예상해보세요.

class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()
# 자식호출