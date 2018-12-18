import requests
import bs4
# ctrl + shift + i
# ctrl + u = 원본보기


url = "https://www.bithumb.com/"

soup = bs4.BeautifulSoup(requests.get(url).text,'html.parser')

names_result = soup.select('.blind')
names = [x.text for x in names_result[3:]]
print("names의 길이\n",len(names))
prices_result = soup.select('.sort_real')
prices = [x.text for x in prices_result]
#print(*prices,sep='\n')
print("prices의 길이\n",len(prices))
with open('bithumb.txt','w') as fileobj:
    for x in range(len(prices)):
        fileobj.write(names[x]+'\t'+prices[x]+'\n')


"""

7% -> 25/30
20% -> 55/60
20% -> 55/60
30% -> 55/60



"""