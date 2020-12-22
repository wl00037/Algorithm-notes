#   要求：两个线程轮流打印数字1-100
#   思路有两个：
#   1、采用锁：Lock
#   2、采用事件，用主线程来控制子线程的执行逻辑

import threading
import queue
import time

# ********************************************************* 方法一：锁 ****************************************************************** #

#   注：Python中threading.Lock作用就是控制一段代码，确保多线程环境下调度不出现混乱，一定要牢记，Lock的作用对象是一段代码块！

#   另外简单说一下：
#       Lock锁会阻塞申请锁的线程的同一代码段的递归执行；
#       RLock锁只会阻塞其他线程代码段执行，不会阻塞同一线程的递归执行，所以RLock也叫递归锁；

Q = queue.Queue()
for i in range(1,100):
    Q.put(i)

lockA=threading.Lock()      #   创建两把锁
lockB=threading.Lock()

def printA():
    lockA.acquire()                 #   LockA锁的是printA中的代码块
    print("printA",Q.get())
    lockB.release()                 #   这里会释放掉LockB，使LockB可以递归继续，如果这里不释放LockB，printB会阻塞，就不会释放LockA，LockA也会阻塞
    printA()                        #   这里我们会发现有递归，但是如果我们递归到printA时，并且还没有释放LockA，那么就会阻塞，知道LockA被释放

def printB():
    lockB.acquire()                 #   LockB锁的是printB的代码块
    print("printB",Q.get())
    lockA.release()                 #   这里释放了LockA，所以PrintA的线程可以继续执行下去，直到LockB的释放，并PrintA自己阻塞到下一次；
    printB()

tA=threading.Thread(target=printA)
tB=threading.Thread(target=printB)
lockB.acquire()
tA.start()
tB.start()

# *********************************************** 方法二：采用事件，用主线程来控制子线程的执行逻辑 *************************************************** #
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