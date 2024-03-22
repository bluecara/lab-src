# 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.

my_list = ["가", "나", "다", "라"]
'''
라 다
다 나
나 가
'''

for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i - 1])