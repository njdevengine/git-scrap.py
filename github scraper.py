#!/usr/bin/env python
# coding: utf-8

# In[242]:


import bs4


# In[243]:


import re


# In[244]:


import time


# In[245]:


from urllib.request import urlopen as uReq


# In[246]:


from bs4 import BeautifulSoup as soup


# In[247]:


my_url = 'https://github.com/orgs/RutgersCodingBootcamp/people?page=1&query=&utf8='


# In[248]:


uReq(my_url)


# In[249]:


uClient = uReq(my_url)


# In[250]:


page_html = uClient.read()


# In[251]:


page_soup = str(soup(page_html, "html.parser"))


# In[252]:


startnum = (page_soup).find('alt="@') +6


# In[253]:


finnum = (page_soup[startnum:]).find('" ')+ startnum


# In[254]:


username = page_soup[startnum:finnum]


# In[255]:


userlink= "https://github.com/" + username


# In[256]:


userlink


# In[277]:


urls = []
for i in range(1,55):
    urls.append('https://github.com/orgs/RutgersCodingBootcamp/people?page='+ str(i) +'&query=&utf8=')


# In[ ]:





# In[283]:


i=0
urls[i]
soup_array = []


# In[ ]:





# In[329]:





# In[330]:





# In[331]:


print(urls[2])


# In[431]:


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


# In[432]:


get_soup()


# In[393]:


n = 0
while n<56:
    n+=1
    print(str(n))


# In[436]:


soup_array[53]

