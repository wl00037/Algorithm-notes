#   归并排序
#   思路：
#   类似于分治法的思路，将一个数组拆分成

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    curr = []
    left = merge_sort(nums[0:len(nums)//2])
    right = merge_sort(nums[len(nums)//2:len(nums)])

    while(len(left)!=0 and len(right)!=0):
        if left[0] < right[0]:
            curr.append(left.pop(0))
        else:
            curr.append(right.pop(0))

    if len(left) != 0:
        curr.extend(left)
    else:
        curr.extend(right)
    return curr

nums = [10,-1,3,2,7,12,-4,0,21,6]
print(merge_sort(nums))

