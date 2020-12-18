#!/usr/bin/env python
# coding: utf-8

# # 6-6. Polling: Use the code in favorite_fruits.py.
# # • Make a list of people who should take the favorite fruit poll. Include some names that are already in the dictionary and some that are not.
# # • Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

# In[3]:


peoples = ["sagar", "dharm", "mehul", "satyam", "jay", "jignesh"]
fav_fruits = {"bhavik": "apple", 
              "mehul": "banana", 
              "jay": "kiwi", 
              "jignesh": "mango", 
              "pruthvi": "orange"}


# In[5]:


for key, value in fav_fruits.items():
    if key in peoples:
        print("Thank you for the taking poll, " + key.title() + ".")
    else:
        print("Hey " + key.title() + ", Would you like to take the poll ?")

