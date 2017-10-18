
import socket
 
s = socket.socket()         
print "Socket successfully created"
 
port = 8080
s.bind(('', port))        
print "socket binded to %s" %(port)
s.listen(5)     
print "socket is listening"
 
while True:
         c, addr = s.accept() 
         print 'Got connection from', addr
         c.send('Fuck you Bitch :P')
         
         c.close()
