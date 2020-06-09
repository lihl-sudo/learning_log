# 建立 python3.8 环境
FROM pypy

# 镜像作者
MAINTAINER lhl 783654214@qq.com

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 将 my_blog 文件夹为工作目录
WORKDIR /app

# 将当前目录加入到工作目录中（. 表示当前目录）
ADD . .

# 利用 pip 安装依赖（- i 表示指定清华源，默认源下载过慢）
RUN pip install -U pip -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple/

#设置环境变量
ENV SPIDER=/app
