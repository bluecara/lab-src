# time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.

import time
import datetime

while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)

'''
2024-04-23 10:32:16.476649
2024-04-23 10:32:17.477308
2024-04-23 10:32:18.477942
2024-04-23 10:32:19.478325
2024-04-23 10:32:20.478857
2024-04-23 10:32:21.479541
'''