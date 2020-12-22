

def bin_search(list,target):

    left = 0
    right = len(list)-1

    while left<=right:

        # mid = round(((left + right) / 2)+0.1,0)     #   计算当前left和right的中间部位
        mid = (left + right) // 2
        tmp = list[mid]

        if tmp == target:       # 如果相同，表示找到了，返回mid，即索引位
            return mid
        if tmp > target:
            right = mid - 1
        else:
            left = mid + 1
    return None

my_list=[1,3,5,7,9]
print(bin_search(my_list,7))