#!/usr/bin/env python
# coding: utf-8

# In[11]:


#ABSTRACT CLASS

from abc import ABC, abstractmethod

class shapes(ABC):
    def nsides(self):
        pass
    class triangle(shapes):
        def nsides(self):
            print("I have three sides")
    class square(shapes):
        def nsides(self):
            print("I have four sides")
    t = triangle()
    t.nsides()
    s = square()
    s.nsides()
    


# In[12]:


#Multilple Inheritence

class Name(object):
     
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
 
#  Sub class 
class Childclass1(Name):
     
    # Constructor
    def __init__(self, name, age):
        Name.__init__(self, name)
        self.age = age
 
    # To get name
    def getAge(self):
        return self.age
 
#  Sub class 
class Childclass2(Childclass1):
     
    # Constructor
    def __init__(self, name, age, address):
        Childclass1.__init__(self, name, age)
        self.address = address
 
    # To get address
    def getAddress(self):
        return self.address       
 

g = Childclass2("Sparsh", 25, "bengaluru") 
print(g.getName(), g.getAge(), g.getAddress())


# In[ ]:





# In[13]:


#Decorartors

def decorator(func):
 
    # firstexec is a Wrapper function in
    # which the argument is called
     
   
    def firstexec():
        print("this is before function execution")
 
        # calling the actual function now
        # inside the wrapper function.
        func()
 
        print("This is after function execution")
         
    return firstexec
 
 
def function2():
    print("This is inside the function decorator")
 
 
# passing 'function2' inside the
# decorator to control  behaviour
function2 = decorator(function2)
 
 

function2()


# In[14]:


#Replce Specific content

file = open("example.txt","w")
file.write("This is a placement assignment")
file.close()

def read_n_replace(file):
    file = open("example.txt","rt")
    data = file.read()
    data = data.replace('placement','screening')
    file.close()
    file = open("example.txt","wt")
    file.write(data)
    file.close()
    return file


# In[ ]:




