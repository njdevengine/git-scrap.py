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

#test reader outputs username as username / and link as userlink
#need to create a loop that loops through all soup array pages
#outputting userlinks to a new array use below as a basis for the reading code
#will save a finnum as a new reading space
#and continue searching document until number is -1 (aka not found)
#when number is -1 else kicks in to go to next page in array

startnum = (page_soup).find('alt="@') +6
finnum = (page_soup[startnum:]).find('" ')+ startnum
username = page_soup[startnum:finnum]
userlink= "https://github.com/" + username
userlinks.append(userlink)

#########
userlinks = []
def extraction():
    startnum = 0
    i = 0
    finnum = 0
    while i < 54:
        if startnum == -1:
            i+=1
            finnum = 0
        else:
            current_soup = soup_array[i]
            print ("searching page number: {}".format(i))
            startnum = current_soup[finnum:].find('alt="@') +6
            finnum = (page_soup[startnum:]).find('" ')+ startnum
            username = page_soup[startnum:finnum]
            userlink= "https://github.com/" + username
            userlinks.append(userlink)
            

##########    

#creates urls for pages 1-54 and saves into urls array
urls = []
for i in range(1,55):
    urls.append('https://github.com/orgs/RutgersCodingBootcamp/people?page='+ str(i) +'&query=&utf8=')
    
i=0
urls[i]

#saves all 54 pages of source code to an array called soup_array
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

