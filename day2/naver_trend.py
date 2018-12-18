# 1. requests에게 naver.com의 요청을 보내서
# 2. 응답받은 문서를 저장하고
# 3. beautifulsoup 패키지를 통해서 정보를 찾기 좋게 만들고
# 4. 그중에서 우리가 원하는 정보를 뽑아온다.

import requests
import bs4 

url = 'https://www.naver.com/'

response = requests.get(url)
print("response \n:",response)
print("text length \n:",len(response.text))

#<span class="ah_k">동성제약</span>
#이 문자열에 불과한 것을 읽을수있도록 하는게 beautifulsoup
#bs4.BeautifulSoup(이쁘게 만들 문서, 'html.parser')
doc = bs4.BeautifulSoup(response.text, 'html.parser')
print("doc length \n:",len(doc))

result = doc.select('.ah_k')
# id는 #기호, class는 .기호
print("1st result \n:",result[0].text)
# 잘 못읽으니까 인코딩타입을 바꿔서 한글로 출력해야함.
# git option -> text -> locale:ko_KR, eucKR
#print("whole result\n",result)

# 5. webbrowser를 통해 1위 검색어를 검색한 결과를 출력하겠다.
# 드래그하고 ctrl+/ 하면 멀티주석됨.
import webbrowser
import random


search_url = "https://search.naver.com/search.naver?query="
for e in random.sample(result,5):
    webbrowser.open(search_url + e.text)

# print(dir(response)) : 어떤걸쓸수있는가?

print("avaliable methods in requests\n",dir(response))
