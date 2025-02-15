# Website for Research Group Based on Django Framework

## Usage

确认你的电脑已经正确安装 Python 3.4 以上的版本。

```
git clone https://github.com/jihenghu/research_group_web.git
```


下载项目后，在命令行中进入项目目录，并创建虚拟环境：

```
python -m venv env
```

运行虚拟环境（Windows环境）:
```
env\Scripts\activate.bat
```

或（Linux环境）：

```
source env/bin/activate
```

自动安装所有依赖项：
```
pip install -r requirements.txt
```

收集静态资源:
```
$ python3 manage.py collectstatic
```

然后进行数据迁移：
```
python3 manage.py makemigrations
python manage.py migrate
```

最后运行测试服务器：

```
python manage.py runserver
```

项目就运行起来了。

数据库文件db.sqlite3以及媒体文件夹media中的内容是方便读者查看示例效果而存在的。

如果你想清除所有数据及媒体文件，将它们直接删除，并运行：

```
python manage.py createsuperuser
```
即可重新创建管理员账号。


启动 nginx 服务：
```
(env) ~$ sudo service nginx start
```

启动 Gunicorn
```
nohup gunicorn --bind 127.0.0.1:8000 rsew.wsgi:application &
```

Refer to [dusai_blog](https://github.com/stacklens/django_blog_tutorial/blob/master/md/40.%E5%B0%86%E9%A1%B9%E7%9B%AE%E9%83%A8%E7%BD%B2%E5%88%B0%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8.md)
