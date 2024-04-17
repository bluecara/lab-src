# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.

def make_url(string) :
    url = "www." + string + ".com"
    return url

result = make_url("naver")
print(result)
# www.naver.com