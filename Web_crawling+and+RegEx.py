
import re
hand=open(r'C:\Users\Ashish\Desktop\Test\Regex_file.txt')

for line in hand:
    line=line.rstrip()
    if re.search('^From', line):
        print (line)

x= 'From ashish222322@gmail.com      '

y=x.split()

y
email=y[1]
email
email=email.split('@')
email[1]

domain=re.findall('@([^ ])*',x)
x

lin='From ashish222322@gmail.com'


y=re.findall('@([^ ]*)',x)
y
import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org',80))
cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

#while True:

while True:
    data=mysock.recv(512)
    if (len(data))<1:
        break
    print (data.decode())
mysock.close()    

