# Question 1


```python
def attach_data(func): 
       func.data = 3
       return func 
  
@attach_data
def add (x, y): 
    return x + y 
print(add(10, 3)) 
print(add.data)
```

    13
    3
    

# Question 2


```python
file = open('niki.txt', 'r')

print(file.read())
try:
    file.write('read is only allowed')
    file.close()          
except :
    print("writing is not enabled")
    
```

    
    writing is not enabled
    
