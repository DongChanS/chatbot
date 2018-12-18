# 1. 나눔로또 api를 통해 우승 번호를 가져온다.
# 2. random으로 생성된 번호와 우승 번호를 비교해서 내가 몇등인지 예측한다.
# - 1등 : 6개
# - 2등 : 5개맞고 + 보너스번호
# - 3등 : 5개
# - 4등 : 4개
# - 5등 : 3개

import random
import json
# json과 딕셔너리의 차이 : json은 그냥 문자이다.
import requests
url = "https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837"
json_phonenumber = "{\"john\":\"01012343959\"}"
# 이런식으로 json은 딕셔너리같은 글자임.
# 그래서 이런 글자로부터 언어가 이해하는 유의미한 자료형으로 바꾸는 작업이 필요함
# 그게 파싱임.
import time
from pprint import pprint
dic_phonenumber = json.loads(json_phonenumber)
#print(dic_phonenumber)

# 인증서의 미스매치때문에 뜨는 오류
# 최근에 인증서가 만료되서 거절되는거임.
# SSLError(CertificateError) : 니가 보낸 호스트는 nlotto인데 여기 인증서는 dhlottery임.
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
print(requests.get(url))
lotto_dict = json.loads(requests.get(url).text)
pprint(lotto_dict)
lotto_numbers = [lotto_dict["drwtNo%s"%(x)] for x in range(1,7)]
lotto_numbers = sorted(lotto_numbers)
bonus = lotto_dict['bnusNo']
print("lotto\n",lotto_numbers)
print("bonus\n",bonus)

"""
1000만번

1등의 개수: 10
2등의 개수: 74
3등의 개수: 2775
4등의 개수: 136718
5등의 개수: 2244839

"""

ranklist = [0 for _ in range(5)]

time1 = time.time()
for _ in range(10**6):
    
    my_numbers = random.sample(range(1,46),6)
    same_count = 12-len(set(my_numbers+lotto_numbers))
    if same_count == 5:
        if bonus in my_numbers:
            ranklist[1] += 1
        else:
            ranklist[2] += 1
    elif same_count == 3:
        # 3 -> 4, 4 -> 3, 6 -> 0
        ranklist[4] += 1
    elif same_count == 4:
        ranklist[3] += 1
    elif same_count == 6:
        ranklist[0] += 1

print('걸린 시간\n',time.time() - time1)

for x in range(len(ranklist)):
    print("%s등의 개수: %s"%(x+1,ranklist[x]))