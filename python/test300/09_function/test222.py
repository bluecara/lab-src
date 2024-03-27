# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.

def print_score(score_list) :
    print(sum(score_list) / len(score_list))

print_score ([1, 2, 3])
# 2.0