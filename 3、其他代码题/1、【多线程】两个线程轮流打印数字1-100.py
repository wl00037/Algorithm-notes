#   要求：两个线程轮流打印数字1-100
#   思路：
#   1、创建两个锁，拿到对方的锁阻塞对方
#   2、在1的前提上，来打印1-100的数字；

import threading
import queue
import time

lockA=threading.Lock()
lockB=threading.Lock()

Q = queue.Queue()
for i in range(1,100):
    Q.put(i)

def printA():
    lockA.acquire()
    print("printA",Q.get())
    lockB.release()
    printA()

def printB():
    lockB.acquire()
    print("printB",Q.get())
    lockA.release()
    printB()

tA=threading.Thread(target=printA)
tB=threading.Thread(target=printB)

lockB.acquire()
tA.start()
tB.start()


