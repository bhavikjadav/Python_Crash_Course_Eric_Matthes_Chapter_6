#!/usr/bin/env python
# coding: utf-8

# # 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

# In[2]:


cities = {"atlanta": {"country": "united states", "population": 10000, "fact": "education"},
          "surat": {"country": "bharat", "population": 100000, "fact": "food"},
          "mumbai": {"country": "bharat", "population": 500000, "fact": "film industry"}}


# In[10]:


for city, info in cities.items():
    print("\n" + city.title() + " : ")
    country = info["country"]
    population = info["population"]
    fact = info["fact"]
    
    print(city.title() + " is in " + country.title() + ".")
    print(city.title() + " contains population of " + str(population) + "+ peoples.")
    print(city.title() + " is famouse for " + fact.title() + ".")

