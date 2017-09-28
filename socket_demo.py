#coding=utf-8

#'a socket demo'

__author__ = 'Wilson'

import socket

#创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM 表示UDP.

#建立连接
s.connect(('www.sina.com.cn', 80))

'''
AF_INET指定使用IPv4协议，IPv6，为AF_INET6

SOCK_STREAM指定使用面向流的TCP协议

80端口是Web服务的标准端口
'''

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接收数据
buffer = []

while True:
    #每次最多接收1k字节
    d = s.recv(1024)

    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

#接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。

#关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

#把接收到的数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)


'''
小结

客户端，要主动连接服务器的IP和指定端口，
对服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。

同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。
'''