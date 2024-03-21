# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.

file_name = "보고서.xlsx"
print("file_name : ", file_name)
a = file_name.endswith("xlsx")
print("xlsx : ", a)
# True
b = file_name.endswith("xls")
print("xls : ", b)
# False