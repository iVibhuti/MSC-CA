#!/usr/bin/env python
# coding: utf-8

# In[1]:


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import cv2
import urllib.request


# In[2]:


try:
    def freq(str1):
        str1 = str.split()          
        str2 = [] 

        for i in str1:
            if i not in str2:
                str2.append(i)
              
        for i in range(0, len(str2)):
            print(str2[i], ':', str.count(str2[i]))
            
except FileNotFoundError:
    print("File Not Found")
    
except TypeError:
    print("File Is Not Valid")


# In[3]:


str ='Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, search engine, cloud computing, software, and hardware. It is considered one of the Big Four technology companies, alongside Amazon, Apple and Facebook.'
freq(str)  


# In[4]:


wordcloud = WordCloud(width=1480, height=1480, max_words=10).generate(str)


# In[5]:


plt.imshow(wordcloud)
plt.show()


# In[ ]:




