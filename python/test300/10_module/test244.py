# 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# 18:35:01

import datetime

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))
# 13:39:36