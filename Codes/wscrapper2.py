from bs4 import BeautifulSoup
import requests
import csv

csv_file=open('new_csv.csv','w',encoding='utf-8')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Heading','Image Link','Content'])

blog_web_html=requests.get('https://www.fonearena.com/blog/#google_vignette').text

soup=BeautifulSoup(blog_web_html,'lxml')


entire_article=soup.find_all('article')

for article in entire_article:
    heading=article.find('h2')

    img_link=article.find('img')['src']

    content=article.find_all('p')

    csv_writer.writerow([heading.text,img_link,content[1].text])

