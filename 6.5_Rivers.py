#!/usr/bin/env python
# coding: utf-8

# # 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# # • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# # • Use a loop to print the name of each river included in the dictionary.
# # • Use a loop to print the name of each country included in the dictionary.

# In[8]:


rivers = {"ganga": "bharat",
          "nile": "egypt", 
          "tapi": "surat"}


# In[9]:


for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title() + ".")


# In[10]:


for river, place in rivers.items():
    print(river.title())


# In[11]:


for river, place in rivers.items():
    print(place.title())

