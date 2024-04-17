# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.

import datetime

now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)
'''
2024-04-12 13:39:08.400949
2024-04-13 13:39:08.400949
2024-04-14 13:39:08.400949
2024-04-15 13:39:08.400949
2024-04-16 13:39:08.400949
'''