
# 题目：四个线程同步打印a b c d
# 解释：线程a打印完a后，线程b打印b，线程c打印c，线程b打印b，一轮后再开始线程a打印a，共10轮；
# 思路：每个线程需要按照顺序通知，未收到通知的不能打印，否则顺序就乱了，所以选择用Event最容易解决；

import threading

a_event = threading.Event()
b_event = threading.Event()
c_event = threading.Event()
d_event = threading.Event()

#   Event()可以创建一个事件管理标志，该标志（event）默认为False；
#   事件主要用于主线程控制其他线程的执行，Event主要提供的三个方法为wait、clear、set；

def print_a(curretn_event, next_event):
    for i in range(3):
        curretn_event.wait()        # 如果event.isSet()==False将阻塞线程
        print('a')
        curretn_event.clear()       # 恢复event的状态值为False
        next_event.set()            # 置event的状态值为True

def print_b(curretn_event, next_event):
    for i in range(3):
        curretn_event.wait()
        print('b')
        curretn_event.clear()
        next_event.set()

def print_c(curretn_event, next_event):
    for i in range(3):
        curretn_event.wait()
        print('c')
        curretn_event.clear()
        next_event.set()

def print_d(curretn_event, next_event):
    for i in range(3):
        curretn_event.wait()
        print('d')
        curretn_event.clear()
        next_event.set()

a_thread = threading.Thread(target=print_a, args=(a_event, b_event))
b_thread = threading.Thread(target=print_b, args=(b_event, c_event))
c_thread = threading.Thread(target=print_c, args=(c_event, d_event))
d_thread = threading.Thread(target=print_d, args=(d_event, a_event))
a_thread.start()        # 执行方法 a_event，并且将线程b的阻塞去除，进入就绪状态
b_thread.start()
c_thread.start()
d_thread.start()
a_event.set()           # 此时要先把线程a的阻塞放开，否则一直都在阻塞中