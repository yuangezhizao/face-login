<?php

ini_set('display_errors', 'off');

include_once 'common.php';
include_once 'MySQL.php';

$arr = array(
    'image_path' => $_GET['image_path'],
    'user_name' => $_GET['user_name'],
);

$faceInfo = Pic::detect($arr['image_path']);

if (count($faceInfo['data']['boxes']) <= 0) {
    $arr = array(
        'code' => -404,
        'msg' => '检测人脸失败，请重试！',
    );
    echo json_encode($arr);
    exit;
}

$registedInfo = Pic::search($arr['image_path']);

if (isset($registedInfo['data'][1][0]) && $registedInfo['data'][1][0] < 1) {
    $userInfo = MySQL::select('face_user', 'id=' . $registedInfo['data'][0][0]);
    $user_name = $userInfo[0]['user_name'];
    $arr = array(
        'code' => -400,
        'msg' => '用户【' . (string)$user_name . '】已存在',
    );
    echo json_encode($arr);
    exit;
}

$id = MySQL::insertData('face_user', $arr);

if ($id) {
    $result = Pic::register($id, $arr['image_path']);
    if ($result['code']) {
        $arr = array(
            'code' => -500,
            'msg' => '添加索引失败',
        );
        echo json_encode($arr);
        exit;
    }
    echo json_encode(array('code' => 0, 'msg' => '用户【' . (string)$arr['user_name'] . '】注册成功！'));
    exit;
} else {
    echo json_encode(array('code' => -500, 'msg' => '数据库错误！'));
    exit;
}
