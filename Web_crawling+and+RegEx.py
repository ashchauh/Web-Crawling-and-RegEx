
# coding: utf-8

# In[8]:


#Regular expression


# In[30]:


import re


# In[31]:


hand=open(r'C:\Users\Ashish\Desktop\Test\Regex_file.txt')


# In[32]:


for line in hand:
    line=line.rstrip()
    if re.search('^From', line):
        print (line)


# In[47]:


x= 'From ashish222322@gmail.com      '


# In[48]:


y=x.split()


# In[49]:


y


# In[50]:


email=y[1]


# In[51]:


email


# In[52]:


email=email.split('@')


# In[53]:


email[1]


# In[64]:


domain=re.findall('@([^ ])*',x)


# In[65]:


x


# In[56]:


import re


# In[66]:


lin='From ashish222322@gmail.com'


# In[67]:


y=re.findall('@([^ ]*)',x)


# In[68]:


y


# In[70]:


import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# In[71]:


mysock.connect(('data.pr4e.org',80))


# In[76]:


cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()


# In[77]:


mysock.send(cmd)


# In[78]:


while True:


# In[79]:


while True:
    data=mysock.recv(512)
    if (len(data))<1:
        break
    print (data.decode())
mysock.close()    

