file_name = "보고서.xlsx"
print("file_name : ", file_name)
a = file_name.endswith(("xlsx", "xls"))
print("xlsx or xls : ", a)
# True
b = file_name.endswith("doc")
print("doc : ", b)
# False