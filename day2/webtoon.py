import requests
import bs4
import re

url = 'https://m.comic.naver.com/webtoon/weekday.nhn?week='

daylist = ['mon','tue','wen','thu','fri','sat','sun']

with open('webtoon_info.txt','w') as fileobj:
    for day in daylist:

        day_url = url+day
        fileobj.write("-----------------------%sday------------------\n"%(day))
        soup = bs4.BeautifulSoup(requests.get(day_url).text,'html.parser')

        #good = soup.select('#pageList > li > div > a > span > img')
        #print(good[0])
        # for x in range(len(good)):
        #     webtoon_name = re.search('alt="(.*?)" height=.*? src="(.*?)" .*',str(good[x])).group(1)
        #     webtoon_link = re.search('alt="(.*?)" height=.*? src="(.*?)" .*',str(good[x])).group(2)
        #     fileobj.write(webtoon_name)
        #     fileobj.write('\n')
        #     fileobj.write(webtoon_link)
        #     fileobj.write('\n')


        # 이렇게 정규식쓸필요없이 해시검색하듯이 ["src"]로 검색하면 잘나옴.
        names = []
        images = []
        
        for e in soup.select('.toon_name'):
            names.append(e.text)
        
        for e in soup.select('.im_br'):
            images.append(e.select_one('img')["src"])

        for name,img in zip(names,images):
            fileobj.write(name + '\n' + img + '\n')
    
