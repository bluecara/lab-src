# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.

data = "039490     "
print("length : ", len(data))
# length :  11
data = data.rstrip()
print(data)
# 039490
print("length : ", len(data))
# length :  6