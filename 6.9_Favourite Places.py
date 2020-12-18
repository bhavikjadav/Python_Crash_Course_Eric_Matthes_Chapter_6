#!/usr/bin/env python
# coding: utf-8

# # 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

# In[9]:


fav_places = {"eric": ["india", "santrioni", "malasiya"],
              "roc": ["california", "las vegas", "san fransisco"],
              "emma": ["india", "austria", "egypt"]}


# In[10]:


for name, places in fav_places.items():
    print("\n" + name.title() + "'s favourite places are : ")
    for place in places:
        print(place.title())

