#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2019/6/4 0004 23:21
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2019 yuangezhizao <root@yuangezhizao.cn>
"""
# 通过 facenet 得到的 512 特征写入 lmdb 文件中
import os

import lmdb

import face_comm


class face_lmdb:
    def add_embed_to_lmdb(self, id, vector):
        self.db_file = os.path.abspath(face_comm.get_conf('lmdb', 'lmdb_path'))
        id = str(id)
        evn = lmdb.open(self.db_file)
        wfp = evn.begin(write=True)
        wfp.put(key=id, value=face_comm.embed_to_str(vector))
        wfp.commit()
        evn.close()


if __name__ == '__main__':
    # 插入数据
    embed = face_lmdb()
    # embed.add_embed_to_lmdb(12, [1, 2, 0.888333, 0.12343430])
    # 遍历
    db_file = os.path.abspath(face_comm.get_conf('lmdb', 'lmdb_path'))
    evn = lmdb.open(db_file)
    wfp = evn.begin()
    for key, value in wfp.cursor():
        print(key, face_comm.str_to_embed(value.decode()))
