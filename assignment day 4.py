#!/usr/bin/env python
# coding: utf-8

# In[7]:


lower = 1042000
upper =702648265 

while(num<=upper + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while (temp > 0):
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if(num == sum):
        print(num)
        break

