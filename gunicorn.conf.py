import multiprocessing

bind = "unix:/tmp/localhost.socket"   #绑定的ip与端口
# bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1    #进程数
print(workers)
loglevel = 'info'
errorlog = '/Users/lihailong/PycharmProjects/learning_log/gunicorn.error.log' #发生错误时log的路径
# accesslog = '/home/xxx/xxx/gunicorn.access.log' #正常时的log路径
proc_name = 'gunicorn_learningct'   #进程名
timeout = 30      #超时
threads = 2 #指定每个进程开启的线程数
