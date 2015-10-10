
# coding: utf-8

# In[1]:

for countdown in 5, 4, 3, 2, 1, "Hello World!":
    print(countdown)


# In[6]:

News = [
    "Yahoo新聞",
    "蘋果新聞",
    "UDN新聞"
    ]
print(News[2])


# In[7]:

joke = {
    "學生": "老師我拉肚子了",
    "老師": "你就不能說的文雅點嗎?",
    "學生": "老師我菊部有降雨",
    "老師": "......",
    }
x = "學生"
print(x, "say:", joke[x])


# In[22]:

import requests
url = "http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=540c0930-f25b-429c-9adf-128225dfe4f4"
response = requests.get(url)
data = response.json()
print(data)


# In[23]:

import this


# In[25]:

8*9


# In[26]:

47


# In[27]:

print(47)


# In[ ]:



