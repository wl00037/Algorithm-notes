
#   假设有两个文件，A和B，文件的结构均为：字符\t字符\t；
#   现在需要找到A和B两个文件中，无法匹配到的行，比如A文件中第一行和B文件中第7行相同，也算匹配成功；

#   注意点以及难点：
#   1、要以行数多的文件作为外循环；
#   2、要注意数组remove的大坑，循环要用一个copy的数组循环，否则会出现remove后数组索引不正确引发的跳过部分元素的问题；

#   先打开A和B两个文件，最后记着处理完关闭
fa = open("A.txt","r")
fb = open("B.txt","r")

#   可以用readline一次读取一行来处理，也可以采用readlines直接返回每行作为一个元素的数组

a_list = fa.readlines()
b_list = fb.readlines()

#   要以行数多的文件来判断，否则会出现之前的行全部匹配，但是行数更多的文件多出来的行数不会被考虑到

#   Python小技巧：多个变量用if定义，要用数组形式，否则报错。
(short,long) = (a_list,b_list) if len(a_list) < len(b_list) else (b_list,a_list)


#   遍历时要以行数多的文件在外循环，保证出现之前全部匹配，导致行数多的文件中多出来的行不被处理
for i in long[:]:
    #   注意：这里复制出一个数组进行遍历，就是为了保证remove原数组后，不会对遍历的数组产生影响，按顺序该怎么遍历怎么遍历；
    #   注意：如果涉及深拷贝用deepcopy即可；浅拷贝用[:]或copy即可；

    for j in short:             #   根据题目要求，b直接用元素组即可，之前删除的不允许再匹配，所以每次用remove后的即可；
        if i == j:
            long.remove(i)
            short.remove(j)
            #   千万注意：这里remove有大坑，要注意；
            #   如果直接操作原数组，当删除后，会出现循环按照索引位遍历下一个，但是数组长度变小，导致会直接跳过被删除前该元素的下一位；
            break       #   continue和break作用域就是本层循环，不会影响到外层循环

print(short,long)       #   remove完的就是无法匹配到的