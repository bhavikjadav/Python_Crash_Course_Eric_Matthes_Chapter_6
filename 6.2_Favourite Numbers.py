#!/usr/bin/env python
# coding: utf-8

# # 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

# In[18]:


fav_numbers = {"bhavik": 1, "mehul": 2, "jay": 3, "jignesh": 4, "pruthvi": 5}


# In[19]:


print(fav_numbers.keys())
print(fav_numbers.values())


# In[20]:


numbers = [ fav_numbers["bhavik"], 
            fav_numbers["mehul"], 
            fav_numbers["jay"], 
            fav_numbers["jignesh"], 
            fav_numbers["pruthvi"] ]


# In[21]:


print(f"Bhavik's favourite number is {numbers[0]}.")
print(f"Mehul's favourite number is {numbers[1]}.")
print(f"Jay's favourite number is {numbers[2]}.")
print(f"Jignesh's favourite number is {numbers[3]}.")
print(f"Pruthvi's favourite number is {numbers[4]}.")

