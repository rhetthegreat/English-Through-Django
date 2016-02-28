from socket import *
a = socket(AF_INET,SOCK_DGRAM)
#a.bind(("",53))
for x in range(100):
    a.sendto("hello",("sankar-manoj.com",53))
