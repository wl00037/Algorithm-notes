#   题目要求：给一个正整数n，要求按照第一行一个数，第二行2个数的规律，打印出正整数n的正三角形；
#   比如：n=11
#   打印结果如下：
#       1
#       2 3
#       4 5 6
#       7 8 9 10
#       11


def GetRegularTriangle(n):
    #   先拿到1-n的数组，用列表推到式
    AllNumberList = [i+1 for i in range(n)]
    result = ""
    start = 1
    while start <= len(AllNumberList):      #   start从1开始逐层+1，只要start<AllNumberList中元素数量，就表示这行是可行的
        current = AllNumberList[:start]
        for j in current:
            result = result + str(j) + " "
        result += "\n"
        AllNumberList = AllNumberList[start:]       #   拿到AllNumberList中的start个元素，并且删除前start个元素
        start += 1

    if len(AllNumberList) > 0:      #   主要兼容如果最终AllNumberList还有剩余元素的情况
        for j in AllNumberList:
            result = result + str(j) + " "
        result += "\n"

    return result

result = GetRegularTriangle(11)
print(result)