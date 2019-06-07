<?php

ini_set('display_errors', 'off');

class Pic
{
    const FACE_SERVER_IP = 'localhost';
    const FACE_SERVER_PORT = 9999;

    static function connect()
    {
        $fd = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
        socket_set_option($fd, SOL_SOCKET, SO_RCVTIMEO, array("sec" => 5, "usec" => 0));
        if (!is_resource($fd)) {
            return false;
        }
        if (!socket_connect($fd, self::FACE_SERVER_IP, self::FACE_SERVER_PORT)) {
            return false;
        }
        return $fd;
    }

    public static function format_data($params)
    {
        $str = json_encode($params);
        $len = strlen($str);
        $packageData = sprintf('%04d%s', $len, $str);
        return array($len + 4, $packageData);
    }

    static function getResult($arr)
    {
        $fd = self::connect();
        if ($fd) {
            list($len, $data) = self::format_data($arr);
            if (socket_write($fd, $data, $len)) {
                $n_len = socket_read($fd, 4);
                if ($n_len > 0) {
                    $data = socket_read($fd, $n_len);
                    $data = str_replace("'", '"', $data);
                    $data = str_replace('(', '[', $data);
                    $data = str_replace(')', ']', $data);
                    return json_decode($data, true);
                }
            }
        } else {
            throw new Exception('function getResult Error！');
        }
    }

    static function search($image_path)
    {
        $arr = array(
            'cmd' => 'search',
            'image_path' => $image_path
        );
        return self::getResult($arr);
    }

    static function register($id, $image_path)
    {
        $arr = array(
            'cmd' => 'register',
            'id' => $id,
            'image_path' => $image_path,
        );
        return self::getResult($arr);
    }

    static function detect($image_path)
    {
        $arr = array(
            'cmd' => 'detect',
            'image_path' => $image_path,
        );
        return self::getResult($arr);
    }

}
