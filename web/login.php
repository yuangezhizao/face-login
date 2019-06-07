<?php

define('WEB_ROOT', dirname(__FILE__));
require WEB_ROOT . '/libs/Smarty.class.php';
include_once 'common.php';
include_once 'MySQL.php';

if (isset($_GET['op']) && $_GET['op'] == 'search') {
    $image_path = $_GET['image_path'];
    $result = Pic::search($image_path);
    if (isset($result['data'][1][0]) && $result['data'][1][0] < 1) {
        $id = $result['data'][0][0];
        $userInfo = MySQL::select('face_user', 'id=' . $id);
        $user_name = $userInfo[0]['user_name'];
        $arr = array(
            'code' => 0,
            'msg' => '【' . (string)$user_name . '】登录成功！',
            'data' => array(
                'id' => $id,
                'rate' => $result['data'][1][0],
            )
        );
        echo json_encode($arr);
    } else {
        $arr = array(
            'code' => -404,
            'msg' => '登录失败，请重试！',
        );
        echo json_encode($arr);
    }
    exit;
}

$smarty = new Smarty;
$smarty->caching = false;
$smarty->cache_lifetime = 1;
if (empty($_GET['op'])) {
    $_GET['op'] = 'login';
}
$smarty->assign('op', $_GET['op']);
$smarty->assign('version', hash_file('crc32', '/data1/face-login/web/js/main.js'));
$smarty->display('login.tpl');
