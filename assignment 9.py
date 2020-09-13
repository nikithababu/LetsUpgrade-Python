#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[6]:


get_ipython().system('pip install pylint')


# In[7]:


get_ipython().run_cell_magic('writefile', 'prime.py', 'import math\ndef is_prime(num):\n    if num < 2:\n        return False\n    for n in range(2, math.floor(math.sqrt(num) + 1)):\n        if num % n == 0:\n            return False\n    return True\nis_prime(2)')


# In[9]:


import prime

prime.is_prime(2)


# # Question 2

# In[22]:


def amg(num):
    arsum = 0
    t = num
    while t > 0:
        d = t % 10
        arsum += d ** 3
        t //= 10
    if num == arsum:
        print(num)
    else:
        pass 

  
for i in range(1,1000):
    x=amg(i)
    
    

