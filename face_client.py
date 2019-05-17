#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2019/5/17 0017 19:15
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2019 yuangezhizao <root@yuangezhizao.cn>
"""
import socket

ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(ip_port)


def test_search():
    str = '{"cmd":"search","pic":"/Users/chenlinzhong/Documents/v_project/t_faceproject/web/images/meizi2.jpeg"}'
    str_len = len(str)
    send_str = "%04d" % str_len + str
    return send_str


def test_add_face():
    str = '{"cmd":"add_index","id":14,"pic":"/Users/chenlinzhong/Documents/v_project/t_faceproject/web/images/meizi2.jpeg"}'
    str_len = len(str)
    send_str = "%04d" % str_len + str
    return send_str


def test_detect_face():
    str = '{"cmd":"face_detect","pic":"/Users/chenlinzhong/Documents/v_project/t_faceproject/web/images/meizi2.jpeg"}'
    str_len = len(str)
    send_str = "%04d" % str_len + str
    return send_str


send_str = test_detect_face()
sk.sendall(send_str)

server_reply = sk.recv(4)
print(server_reply + '\n')

server_reply = int(server_reply)
server_reply = sk.recv(server_reply)
print(server_reply + '\n')

sk.close()
