#   快速排序
#   思路：
#   1、选择一个目标值，将大于目标值的都放到目标值右侧，小于目标值的都放到目标值左侧，当left和right碰头后就是目标值的位置；
#   2、接着通过递归的方法对目标值左、右两部分数组继续求解；


def quick_sort(array,start,end):

    if start >= end:
        return array

    mid_data,left,right = array[start],start,end

    while(left < right):
        # 外层的while + 内层左右两次的while，可以保证本次的mid_data最终找到它的正确位置

        while(left < right and array[right] >= mid_data):
            right -= 1
        # 从右向左，找到第一个比mid_data小的，right索引位的值放到left索引位，此时right索引位等于是空的
        array[left] = array[right]

        while(left < right and array[left] <= mid_data):
            left += 1
        # 从左向右，找到第一个比mid_data大的，上面的while结束后，right索引位是空的，所以将这个大于mid_data的放到right索引位，此时的left索引位又空余出来
        array[right] = array[left]

    # 到此处，所有大于mid_data的都放到了右边，小于mid_data的都放到了左边，最后剩下的那个right索引位，就是mid_data最合适的位置
    array[right] = mid_data

    # 递归，分别处理right左边和右边的两个子数组
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

    return array

if __name__=="__main__":
    array=[30,24,5,5,-18,36,12,-42,39]
    print(quick_sort(array,0,len(array)-1))









