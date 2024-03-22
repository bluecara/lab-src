# 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 파일 in 리스트:
    이름 = 파일.split(".")
    if 이름[1] == "h":
        print(파일)
# intra.h
# define.h