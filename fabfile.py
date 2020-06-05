from fabric2 import Connection

# GIT_REPO = "https://github.com/lihl-sudo/learning_log.git"

user = 'u0_a261'
password = 'lhl666666'
# 填写你自己的主机对应的域名
host = '192.168.144.7'
# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
port = '8022'


def main():
    # source_folder = ''
    conn = Connection(
        user=user,
        host=host,
        port=port,
        connect_kwargs={
            "password": password})
    # conn.run('ln -s ~/sites/learning_log/nginx.conf $PREFIX/etc/nginx/servers/learning_log.conf')
    # conn.run("")
    # conn.run("""source ~/.virtualenvs/l_l/bin/activate &&
    #             cd ~/sites/learning_log/ && ls &&
    #             pip list && pip install --upgrade -r requirements.txt && pip list""")
    # run('cd %s && git pull' % source_folder)
    # run("""
    #     cd {} &&
    #     ../env/bin/pip install -r requirements.txt &&
    #     ../env/bin/python3 manage.py collectstatic --noinput &&
    #     ../env/bin/python3 manage.py migrate
    #     """.format(source_folder))
    # sudo('restart gunicorn-demo.zmrenwu.com')
    # sudo('service nginx reload')


if __name__ == '__main__':
    main()
