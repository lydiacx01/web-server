#!/usr/bin/env python
# -*- coding: utf-8 -*-

'web server from scratch'

__author__ = 'lydiacx_develop@outlook.com'

import socket

HOST, PORT = '', 8081

#设置socket的address是Ipv4,
#SOCK_STREAM即为socket类型中的TCP数据传输协议, SOCK_DGRAM是udp协议传输
#0是协议数字，一般是0；
#配置文件，若指定了，则会忽略前3个参数的值
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0, None)

#在socket级别上，设置选项SO_REUSEADDR的值为1，即开启地址复用
#作用是将多个socket绑定到同一个端口上，只有最后一个socket能正常接收数据
# 主要是预防服务器重启时，之前的socket未释放，而导致重启服务器时报错--需等前socket释放后再释放
# 还有其他作用
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#socket绑定到地址
listen_socket.bind((HOST,PORT))
#允许socket去接收连接，参数backlog>=0;如果超过backlog个连接没接受，则拒绝新连接
listen_socket.listen(1)

#help(socket.socket)

while True:
    client_conn, client_addr = listen_socket.accept()
    print('the accept returns=', client_conn, '======address=', client_addr)
    
    #最好是2的指数，比较小的OK，比如4096
    request = client_conn.recv(1024)

    print('the request=', request)

    http_response = '''
    HTTP/1.1 200 OK
    Hello, my first web server says hello!
    '''
    client_conn.sendall(http_response.encode())
    client_conn.close()
