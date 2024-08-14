from bs4 import BeautifulSoup
import requests
import csv
source=requests.get('https://www.fonearena.com/blog/').text
soup=BeautifulSoup(source,'lxml')

csv_file=open('scrape_csv.csv','w',encoding='utf-8')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['heading','image link','content'])

articles=soup.find_all('article')
for article in articles:

    heading=article.h2.text

    print("heading:",heading)
    print()


    try:
        image_link=article.find('div',class_='entry-content').p.img['src']
        
        
    except Exception as e:
        image_link=None
        print("image-link:",image_link)
        print()

    
    content=article.find_all('p')[1].text
    print("content:",content)
    print()
    print("----------------------------")
    csv_writer.writerow([heading,image_link,content])
    
csv_file.close()


