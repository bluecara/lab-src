# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.

file_name = "2020_보고서.xlsx"
print("file_name : ", file_name)
a = file_name.startswith("2020")
print("2020 : ", a)
# True
b = file_name.startswith("2021")
print("2021 : ", b)
# False