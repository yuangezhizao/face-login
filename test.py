#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2019/5/17 0017 19:48
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2019 yuangezhizao <root@yuangezhizao.cn>
"""
import face_handler

retData = face_handler.detect_face('/Users/chenlinzhong/Documents/v_project/t_faceproject/web/images/meizi2.jpeg')


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
