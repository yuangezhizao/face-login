#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2019/6/4 0004 20:57
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2019 yuangezhizao <root@yuangezhizao.cn>
"""
import os

import cv2
import mxnet as mx

import face_comm
from mtcnn.mtcnn_detector import MtcnnDetector

model = os.path.abspath(face_comm.get_conf('mtcnn', 'model'))


class Detect:
    def __init__(self):
        self.detector = MtcnnDetector(model_folder=model, ctx=mx.cpu(0), num_worker=4, accurate_landmark=False)

    def detect_face(self, image):
        img = cv2.imread(image)
        results = self.detector.detect_face(img)
        boxes = []
        key_points = []
        if results is not None:
            # box 框
            boxes = results[0]
            # 人脸五个关键点
            points = results[1]
            for i in results[0]:
                faceKeyPoint = []
                for p in points:
                    for i in range(5):
                        faceKeyPoint.append([p[i], p[i + 5]])
                key_points.append(faceKeyPoint)
        return {'boxes': boxes, 'face_key_point': key_points}


if __name__ == '__main__':
    pic = 'D:\\yuangezhizao\\Documents\\PycharmProjects\\face-login\\web\\images\\meizi2.jpeg'
    detect = Detect()
    result = detect.detect_face(pic)
    print(result)
