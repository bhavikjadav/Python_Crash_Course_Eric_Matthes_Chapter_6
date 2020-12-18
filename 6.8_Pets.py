#!/usr/bin/env python
# coding: utf-8

# # 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

# In[1]:


dog = {"type": "lebra", "owner": "garic"}
cat = {"type": "persian", "owner": "matthes"}
elephant = {"type": "mammals", "owner": "kinn"}


# In[2]:


pets = [dog, cat, elephant]


# In[3]:


for pet in pets:
    print(pet)

