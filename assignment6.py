#!/usr/bin/env python
# coding: utf-8

# In[18]:


class bank_acc:
    def __init__(m):
        m.user_name="nikitha"
        m.bal=500000
    def deposit(m,amt):
        m.bal=m.bal+amt
        print("-----deposit-----\n Balance=",m.bal)
    def withdrawl(m,wamt):
        if(wamt<=m.bal):
            m.bal=m.bal-wamt
            print("__withdrawl__\n Balance:",m.bal)
        else:
            print("invalid amt")
m.deposit(7000)
m.withdrawal(2000)
m.deposit(7000)
m.deposit(7000)


# In[ ]:


m.deposit(7000)


# In[19]:


m.withdrawal(700000)


# In[20]:


import math
def __init__(m,radius,height):
    m.r=radius
    m.h=height
pi=math.pi
class cone:
    def area(m):
        l=math.sqrt(2*(m.r)+2*(m.h))
        area=pi*m.r*m.r+pi*m.r*m.l
        print("the surface area of cone:",area)
    def volume(m):
        volume=(1/3)*pi*m.r*m.r*m.h
        print("the volume of cone:",volume)
radius=int(input())
height=int(input())
obj=cone(radius,height)
print(m.volume())
print(m.area())


# In[ ]:




