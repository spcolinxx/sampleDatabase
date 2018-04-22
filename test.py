import threading,queue,datetime

start_time=datetime.datetime.now()

myqueue=queue.Queue(maxsize=-1)

def print_char():
    myqueue.put("a")




def print_num():
    myqueue.put("1")

t1=threading.Thread(target=print_num,args=())
t2=threading.Thread(target=print_char,args=())

t1.start()
t2.start()
t1.join()
t2.join()

print(myqueue.get())
print(myqueue.get())

end_time=datetime.datetime.now()

print((end_time-start_time))