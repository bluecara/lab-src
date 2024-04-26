# 바탕화면에 생성한 '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장해보세요.

f = open("C:/Users/USER/Desktop/매수종목1.txt", encoding="utf-8")
lines = f.readlines()   # python list

codes = []
for line in lines:
    code = line.strip()  #'\n'
    codes.append(code)

print(codes)

f.close()

