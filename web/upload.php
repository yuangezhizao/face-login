<?php

ini_set('display_errors', 'on');

function save($image_base64, $image_path)
{
    if (preg_match('/^(data:\s*image\/(\w+);base64,)/', $image_base64, $result)) {
        $type = $result[2];
        $new_file = $image_path . "/";
        if (!file_exists($new_file)) {
            mkdir($new_file, 0700, true);
        }
        $new_file = $new_file . time() . ".{$type}";
        if (file_put_contents($new_file, base64_decode(str_replace($result[1], '', $image_base64)))) {
            return $new_file;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

$arr = array(
    'code' => 0,
    'data' => array('image_path' => save($_POST['image_base64'], '/data1/face-login/web/images')),
);

echo json_encode($arr);
exit;
