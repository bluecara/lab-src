# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은? ")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")
# 좋아하는 과일은? 사과
# 정답입니다.
# 좋아하는 과일은? 바나나
# 오답입니다.