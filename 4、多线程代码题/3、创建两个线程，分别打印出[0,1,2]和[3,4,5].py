
# 题目：创建两个线程，分别打印出[0,1,2]和[3,4,5]

import threading

lock = threading.Lock()
l = [0,1,2,3,4,5]

def getNum(thread_name):
    lock.acquire()
    print(thread_name + "线程打印：",l.pop(0))
    print(thread_name + "线程打印：" ,l.pop(0))
    print(thread_name + "线程打印：" ,l.pop(0))
    lock.release()

t1 = threading.Thread(target=getNum,args=("t1",))
t2 = threading.Thread(target=getNum,args=("t2",))
t1.start()
t2.start()


