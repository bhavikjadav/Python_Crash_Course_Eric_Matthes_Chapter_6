#!/usr/bin/env python
# coding: utf-8

# # 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

# In[5]:


glossary = {"print": "for printing a statement",
           "sort": "to sort a list in a ascending order",
           "title": "to change the manner of string in titlecase",
           "list": "to create a list",
           "lower": "to change the manner of string in lowercase"}


# In[6]:


for key, values in glossary.items():
    print(key + " " + values.title() + ".")

