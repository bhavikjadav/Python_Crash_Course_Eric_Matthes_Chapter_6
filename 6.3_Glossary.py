#!/usr/bin/env python
# coding: utf-8

# # 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# # • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# # • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

# In[8]:


glossary = {"print": "for printing a statement",
           "sort": "to sort a list in a ascending order",
           "title": "to change the manner of string in titlecase",
           "list": "to create a list",
           "lower": "to change the manner of string in lowercase"}


# In[9]:


print("print : " + glossary["print"].title())
print("sort : " + glossary["sort"].title())
print("title : " + glossary["title"].title())
print("list : " + glossary["list"].title())
print("lower : " + glossary["lower"].title())

