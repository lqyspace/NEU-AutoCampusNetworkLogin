# NEU-AutoCampusNetworkLogin
东北大学校园网自动登录认证脚本

## Environment
```
python==3.8
selenium
```

## 运行
```
python jobSelenium.py -n 学号 -p 密码
```

## 发送主机ip的邮件
```
python smtp.py --ip ip地址 --sender 发送者邮件地址 --receivers 接受者邮件地址 --mail_host 发送者邮件服务器地址 --mail_port 服务器端口号 --mail_user 发送者账户 --mail_pass 发送者账户密码
```

