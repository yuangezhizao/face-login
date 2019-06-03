#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2019/6/3 0003 16:59
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2019 yuangezhizao <root@yuangezhizao.cn>
"""
import socket

ip_port = ('txy.yuangezhizao.cn', 9999)
sk = socket.socket()
sk.connect(ip_port)


def test_search():
    str = "{'cmd':'search','pic':'/data1/face-login/web/images/meizi2.jpeg'}"
    return '%04d' % len(str) + str


def test_add_index():
    str = "{'cmd':'add_index','id':14,'pic':'/data1/face-login/web/images/meizi2.jpeg'}"
    return '%04d' % len(str) + str


def test_face_detect():
    str = "{'cmd':'face_detect','pic':'/data1/face-login/web/images/meizi2.jpeg'}"
    return '%04d' % len(str) + str


send_str = test_face_detect().encode()
sk.sendall(send_str)

len = sk.recv(4).decode()
print(len)

data = sk.recv(int(len)).decode()
print(data)

sk.close()
