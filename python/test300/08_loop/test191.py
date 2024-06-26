# data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

# 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.

for row in data:
    for col in row:
        print(col * 1.00014)
'''
2000.28
3050.427
2050.2870000000003
1980.2772
7501.05
2050.2870000000003
2050.2870000000003
1980.2772
15452.163
15052.107
15552.177
14902.086000000001
'''