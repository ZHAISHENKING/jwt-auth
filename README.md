# JWT-AUTH

关键词： `flask`,`mongoengine`,`Pyjwt`,`auth`,`RestFul`		



使用flask框架实现登录注册并实现token校验的flask-restful项目



用户登录过程

<img src="http://qiniu.s001.xin/flask/jwt.png">

项目目录

```
.

├── README.md

├── pycache

├── app

│   ├── init.py

│   ├── pycache

│   ├── auth

│   ├── common.py

│   ├── config.py

│   └── users

├── manage.py

└── requirements.txt

```



1.运行`pip install -Ur requirements.txt`

2.安装mongo并启动

3.运行`python manange runserver`