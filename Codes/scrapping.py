from bs4 import BeautifulSoup 

with open('Html//simple.html') as html:
    soup=BeautifulSoup(html,'lxml')

articles=soup.find_all('div',class_='article')
for article in articles:
   print(article.h1.text)
   print(article.p.text)
   print()



