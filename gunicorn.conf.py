import multiprocessing
# import gevent.monkey
# gevent.monkey.patch_all()

bind = "unix:/tmp/localhost.socket"   #绑定的ip与端口
# bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1  # 进程数
print(workers)
loglevel = 'info'
errorlog = './deployment/tmp/logs/gunicorn.error.log'  # 发生错误时log的路径
accesslog = './deployment/tmp/logs/gunicorn.access.log'  # 正常时的log路径
pidfile='./deployment/tmp/learning_log.pid' # 设置进程文件目录
# worker_class='gunicorn.workers.ggevent.GeventWorker' # 工作模式协程
proc_name = 'learning_log'  # 进程名
timeout = 30  # 超时
threads = 2  # 指定每个进程开启的线程数
x_forwarded_for_header = 'X-FORWARDED-FOR'