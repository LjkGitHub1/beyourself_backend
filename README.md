# beyourself_backend
认知功能与精神健康测训平台后端

# 环境依赖
Python >= 3.8.0 (推荐3.9.7)
Mysql >= 5.7.0 (可选，默认数据库sqlite3，推荐8.0版本)

# 后端配置env.py文件
1. 进入后端项目目录:cd backend
2. 在项目根目录中，复制 ./conf/env.example.py 文件为一份新的到 ./conf/env.py 下，并重命名为env.py
    # # 数据库用户名
    DATABASE_USER = "beyourself"
    # # 数据库密码
    DATABASE_PASSWORD = "123456"

# 后端运行
1. 进入后端项目目录:cd backend

2. 安装依赖环境: pip3 install -r requirements.txt

3. 执行迁移命令: python3 manage.py makemigrationspython3 manage.py migrate

4. 初始化数据: python3 manage.py init

5. 初始化省市县数据: python3 manage.py init_area

6. 启动项目: python3 manage.py runserver 0.0.0.0:8000