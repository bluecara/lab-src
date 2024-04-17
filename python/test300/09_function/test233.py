# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.

def make_list (string) :
    my_list = []
    for 변수 in string :
        my_list.append(변수)
    return my_list

result = make_list("abcd")
print(result)
# ['a', 'b', 'c', 'd']