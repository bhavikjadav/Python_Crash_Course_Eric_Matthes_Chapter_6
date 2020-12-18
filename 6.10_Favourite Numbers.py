#!/usr/bin/env python
# coding: utf-8

# # 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

# In[1]:


fav_numbers = {"bhavik": [10, 20, 30],
               "mehul": [40, 50, 60],
               "pruthvi": [70, 80, 90],
               "jay": [100, 110, 120]}


# In[3]:


for name, numbers in fav_numbers.items():
    print("\n" + name.title() + "'s favourite numbers are : ")
    for number in numbers:
        print(number)

