#!/usr/bin/env python
# coding: utf-8

# In[9]:


file = open("example.txt","w")
file.write("This is a placement assignment")
file.close()

def read_n_replace(file):
    file = open("example.txt","rt")
    data = file.read()
    data = data.replace('placement','screening')
    file.close()
    file = open("example.txt","wt")
    file.write(data)
    file.close()
    return file


# In[5]:





# In[8]:





# In[ ]:




