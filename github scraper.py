import bs4
import re
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://github.com/orgs/RutgersCodingBootcamp/people?page=1&query=&utf8='

uReq(my_url)

uClient = uReq(my_url)

page_html = uClient.read()

page_soup = str(soup(page_html, "html.parser"))

startnum = (page_soup).find('alt="@') +6
finnum = (page_soup[startnum:]).find('" ')+ startnum
username = page_soup[startnum:finnum]

userlink= "https://github.com/" + username

urls = []
for i in range(1,55):
    urls.append('https://github.com/orgs/RutgersCodingBootcamp/people?page='+ str(i) +'&query=&utf8=')
    
i=0
urls[i]

soup_array = []
def get_soup():
    n=0
    while n <54:
        my_url = urls[n]
        uReq(my_url)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = str(soup(page_html, "html.parser"))
        soup_array.append(page_soup)
        print(urls[n])
        print(page_soup[:10])
        n += 1
        print('saving soup number '+str(n))
        time.sleep(5)

get_soup()

n = 0
while n<56:
    n+=1
    print(str(n))

soup_array[53]

