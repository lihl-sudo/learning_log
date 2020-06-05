import multiprocessing

bind = "127.0.0.1:8001"   #绑定的ip与端口
workers = multiprocessing.cpu_count() * 2 + 1    #进程数
print(workers)
errorlog = '/data/data/com.termux/files/home/sites/learning_log/gunicorn.error.log' #发生错误时log的路径
loglevel = 'warning'
# accesslog = '/home/xxx/xxx/gunicorn.access.log' #正常时的log路径
proc_name = 'gunicorn_learningct'   #进程名
timeout = 30      #超时
threads = 2 #指定每个进程开启的线程数
