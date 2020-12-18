#!/usr/bin/env python
# coding: utf-8

# # 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

# In[1]:


peoples = [{"firstname": "mehul", "lastname": "rana", "age":19, "city": "surat"},
           {"firstname": "bhavik", "lastname": "jadav", "age":19, "city": "surat"},
           {"firstname": "erica", "lastname": "punta", "age":21, "city": "atlanta"}]


# In[2]:


for people in peoples:
    print(people)

