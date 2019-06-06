#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2019/6/6 0006 14:51
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2019 yuangezhizao <root@yuangezhizao.cn>
"""
import face_handler

pic = 'D:\\yuangezhizao\\Documents\\PycharmProjects\\face-login\\web\\images\\meizi2.jpeg'

retData = face_handler.detect_face(pic)


def trans_string(retData):
    fp = open('json_tmp.txt', 'w')
    retData['boxes'] = retData['boxes'].tolist()
    print(retData, file=fp)
    fp.close()
    return get_json_data()


def get_json_data():
    f = open('json_tmp.txt')
    line = f.readline()
    f.close()
    str_len = len(line) - 1
    str_len = "%04d" % str_len
    return str_len + line


print(trans_string(retData))
