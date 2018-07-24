import threading

def test(para):
    print(para)



for i in range(100):
    t=threading.Thread(target=test,args=(i,))
    t.start()

