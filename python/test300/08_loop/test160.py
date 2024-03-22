# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 파일 in 리스트:
    이름 = 파일.split(".")
    if 이름[1] == "h" or 이름[1] == "c":
        print(파일)
# intra.h
# intra.c
# define.h