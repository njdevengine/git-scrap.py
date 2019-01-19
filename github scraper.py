##curl -i -u njdevengine https://api.github.com/orgs/RutgersCodingBootcamp/members
##import os
##os.system("curl -i -u your_github_username:your_github_password https://api.github.com/users/usernamegoeshere")
## sample excel formula ="os.system("""&D1&""")"
##this allows you to run command line from python3

##generate your requests
##apiurls = []
##for i in range(1,55):
##    apiurls.append('curl -i -u username:pass https://api.github.com/organizations/14036175/members?page='+ str(i))

import bs4
import re
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

####SITE LOGIN####
import time
from splinter import Browser
executable_path = 'chromedriver'

browser = Browser('chrome')

url = "https://github.com/login"
browser.visit(url)

browser.fill('login', 'your_username')
browser.fill('password', 'your_creds')

button = browser.find_by_name('commit')
button.click()

########



my_url = 'https://github.com/orgs/RutgersCodingBootcamp/people?page=1&query=&utf8='

uReq(my_url)

uClient = uReq(my_url)

page_html = uClient.read()

page_soup = str(soup(page_html, "html.parser"))

#next I need my scraping to be part of a request session

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
            

#new search '"link_type:self" href="/'

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

