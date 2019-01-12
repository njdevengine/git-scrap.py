#!/usr/bin/env python
# coding: utf-8

# In[113]:


import bs4


# In[114]:


import re


# In[231]:


import time


# In[25]:


from urllib.request import urlopen as uReq


# In[26]:


from bs4 import BeautifulSoup as soup


# In[27]:


my_url = 'https://github.com/orgs/RutgersCodingBootcamp/people?page=1&query=&utf8='


# In[115]:


uReq(my_url)


# In[29]:


uClient = uReq(my_url)


# In[30]:


page_html = uClient.read()


# In[101]:


page_soup = str(soup(page_html, "html.parser"))


# In[144]:


startnum = (page_soup).find('alt="@') +6


# In[145]:


finnum = (page_soup[startnum:]).find('" ')+ startnum


# In[147]:


username = page_soup[startnum:finnum]


# In[151]:


userlink= "https://github.com/" + username


# In[153]:


userlink


# In[166]:


urls = []
for i in range(1,55):
    urls.append('https://github.com/orgs/RutgersCodingBootcamp/people?page='+ str(i) +'&query=&utf8=')


# In[ ]:





# In[218]:


i=0
urls[i]


# In[239]:


soup_array = []
def get_soup():
    i = 0
    my_url=urls[i]
    while i<56:
        uReq(my_url)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = str(soup(page_html, "html.parser"))
        soup_array.append(page_soup)
        i+1
        time.sleep(5)
    


# In[ ]:


get_soup()


# In[ ]:


soup_array

