#   归并排序
#   思路：
#   1.将数组从中间划分成两个子数组
#   2.递归，再将两个子数组分别划分成2个更小的子数组，直到数字中剩下一个元素
#   3.再将子数组两两排序合并，最终返回一个完整且排序完成的数组

def merge_sort(array):

    # 当array的长度为1，也就是递归的出口
    if len(array) == 1:
        return array

    # left和right是将本次array拆分成两个子数组排序后的结果
    left = merge_sort(array[0:len(array)//2])
    right = merge_sort(array[len(array)//2:len(array)])

    current = []

    while(len(left) != 0 and len(right) != 0):

        if left[0] < right[0]:
            current.append(left.pop(0))
        else:
            current.append(right.pop(0))

    # 当left或right其中一个已经为空，则直接将另一个append到current即可，left和right的排序则完成
    if len(left) != 0:
        current.extend(left)
    else:
        current.extend(right)

    return current

if __name__ == "__main__":

    array = [10,-1,3,2,7,12,-4,0,21,6]
    print(merge_sort(array))

  
