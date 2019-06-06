<!DOCTYPE html>
<html>
<head>
    <meta name="google-site-verification" content="r60E4sFJHchDyFugnQqJuemmhx_13jgS6sVejKN2ZU0"/>
    <meta name="baidu-site-verification" content="Z3N5kBpPuH" />
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <title>人脸检测与识别的研究与应用</title>
    <meta name="keywords" content="远哥应用,yuangezhizao,远哥制造的实验室">
    <meta name="description" content="远哥应用，远哥制造，远哥制造的实验室">
    <meta name="author" content="yuangezhizao"/>
    <meta name="Copyright" content="Copyright yuangezhizao All Rights Reserved."/>
    <link rel="icon" href="https://i1.yuangezhizao.cn/Win-10/camera.jpeg!webp?imageMogr2/thumbnail/50x/interlace/1"
          type="image/x-icon"/>
    <link rel="shortcut icon"
          href="https://i1.yuangezhizao.cn/Win-10/camera.jpeg!webp?imageMogr2/thumbnail/50x/interlace/1"
          type="image/x-icon"/>
    <link rel="dns-prefetch" href="//lab.yuangezhizao.cn">
    <link rel="dns-prefetch" href="//www.yuangezhizao.cn">
    <link rel="dns-prefetch" href="//txy.yuangezhizao.cn">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link rel="stylesheet" href="../css/main.css">
    <!--<link rel="stylesheet" href="../css/bootstrap.min.css">-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css">
    <!--<script src="../js/jquery.min.js"></script>-->
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.4.1/dist/jquery.min.js"></script>
    <!--<script src="../js/bootstrap.min.js"></script>-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js"></script>
    <!--<script src="../js/ccv.js"></script>-->
    <script src="https://cdn.jsdelivr.net/npm/ccv@1.0.0/js/ccv.min.js"></script>
    <!--<script src="../js/cascade.js"></script>-->
    <script src="https://cdn.jsdelivr.net/npm/cascade@0.7.8/dist/scripts/modules/Cascade.min.js"></script>
    <!--<script src="../js/jquery.facedetection.js"></script>-->
    <script src="https://cdn.jsdelivr.net/npm/jquery.facedetection@2.0.3/dist/jquery.facedetection.min.js"></script>
</head>
<body>
<div id="canvas-container"></div>
<input type="hidden" value="{$op}" id="op">
<div id="tab-container">
    <ul id="myTab" class="nav nav-tabs">
        <li class="{if $op =='login' } active{/if}">
            <a href="#home" data-toggle="tab" class="btn-tab" data-op="login">
                登录
            </a>
        </li>
        <li class="{if $op =='register' } active{/if}"><a href="#ios" data-toggle="tab" class="btn-tab"
                                                          data-op="register">注册</a></li>
    </ul>
    <div id="myTabContent" class="tab-content">
        <div class="tab-pane fade  {if $op =='login' } in active{/if}" {if $op !='login' }style="display: none" {/if}
             id="home">
            <form class="form-horizontal" role="form" style="margin-top: 30px">
                <div class="video-container-2">
                    <img src="https://i1.yuangezhizao.cn/Win-10/camera.jpeg!webp?imageMogr2/thumbnail/50x/interlace/1"
                         id="login-logo"/><br>
                    <video id="video2" width="400" height="300" muted class="abs" style="display: none;"></video>
                    <canvas id="canvas2" width="400" height="300"
                            style="margin-bottom: 30px"></canvas>
                    <br>
                    <a href="#" class="find-face" style="display: none;color: #ff0000">重新扫描</a>
                </div>
            </form>
        </div>
        <div class="tab-pane fade  {if $op =='register' } in active{/if}" {if $op !='register' } style="display: none" {/if}
             id="ios">
            <form class="form-horizontal" role="form" style="margin-top: 30px">
                <div class="form-group">
                    <div class="col-sm-10 r-camera">
                        <img src="https://i1.yuangezhizao.cn/Win-10/camera.jpeg!webp?imageMogr2/thumbnail/50x/interlace/1">
                    </div>
                </div>
            </form>
            <form class="form-horizontal" role="form" style="margin-top: 30px">
                <div class="video-container" style="display: none">
                    <video id="video" width="400" height="300" muted class="abs"></video>
                    <canvas id="canvas" width="400" height="300"></canvas>
                    <br>
                    <a href="#" class="find-face" style="display: none;color: #ff0000">重新扫描</a>
                </div>
            </form>
            <form class="form-horizontal" role="form" style="margin-top: 30px">
                <div class="form-group">
                    <label for="firstname" class="col-sm-2 control-label">用户名</label>
                    <div class="col-sm-10">
                        <input type="text" class="form-control user_name"
                               placeholder="请输入用户名 " style="width: 200px" value="">
                    </div>
                </div>
            </form>
            <div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                    <button type="submit" class="btn btn-default btn-redis">注册</button>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="../js/main.js?v={$version}"></script>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-83264206-13"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'UA-83264206-13');
    var _hmt = _hmt || [];
    (function () {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?6f42275dcf3ae1bf27db1011e8c37750";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(hm, s);
    })();
</script>
</body>
</html>
