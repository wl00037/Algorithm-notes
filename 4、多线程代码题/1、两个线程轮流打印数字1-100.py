#   要求：两个线程轮流打印数字1-100
#   思路有两个：
#   1、采用锁：Lock
#   2、采用事件，用主线程来控制子线程的执行逻辑

import threading
import queue
import time


lockA=threading.Lock()
lockB=threading.Lock()

Q = queue.Queue()
for i in range(1,100):
    Q.put(i)


# 方法一：采用锁
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

# ***************************方法二：采用事件，用主线程来控制子线程的执行逻辑*************************************

Q = queue.Queue()
for i in range(1,101):
    Q.put(i)

event_a = threading.Event()     # 默认wait()的标志都是False，即阻塞
event_b = threading.Event()

def printNumber(thread_name,current_event,next_event):
    while not Q.empty():        # 通常用while not q.empty()来判断Queue是否已经为空；
        current_event.wait()
        if Q.empty():           # 这里要注意：由于thrad阻塞，只有在这个位置才能保证线程a和b继续从list中pop，如果不做判断会导致pop报错，list为空
            break
        print(thread_name,"：",Q.get(True,1))      # 用Queue的get时候要注意：当Queue为空时调用get会阻塞，用get(True,1)会抛出错误，否则会长时间阻塞到有数据可用；
        current_event.clear()
        next_event.set()

thread_a = threading.Thread(target=printNumber,name="Thread A",args=("线程A",event_a,event_b))
thread_b = threading.Thread(target=printNumber,name="Thread B",args=("线程B",event_b,event_a))
thread_a.start()
thread_b.start()
event_a.set()       #   把事件A的阻塞干掉，这样就可以正常跑event_a了