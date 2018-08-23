# coding:utf-8

import os

# Application配置参数,配置模板路径,添加混淆密码加密字符串
#cookie_secret 用uuid 随机生成一个字符串,双重拼接,世界独一无二的字符串,然后通过base64加密
#template_path=os.path.join(os.path.dirname(__file__), "template")
settings = dict(
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret="FhLXI+BRRomtuaG47hoXEg3JCdi0BUi8vrpWmoxaoyI=",
        xsrf_cookies=True,
        debug=True
    )


# 数据库配置参数
mysql_options = dict(
    host="127.0.0.1",
    database="ihome",
    user="root",
    password=""
)

# Redis配置参数
redis_options = dict(
    host="127.0.0.1",
    port=6379
)

# 日志配置
log_path = os.path.join(os.path.dirname(__file__), "logs/log")
log_level = "debug"

# 密码加密密钥
passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="