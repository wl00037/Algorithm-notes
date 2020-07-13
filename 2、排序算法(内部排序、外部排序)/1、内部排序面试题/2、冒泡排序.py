#   冒泡排序
#   思路：
#   外层遍历的索引位置上不断和内层遍历的值比较，保证外层遍历所处的索引位上一定是最小的值；
#   时间复杂度 O(n^2)

def bubble_sort(nums):
    if len(nums) == 0:
        return nums
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[j] < nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

nums = [10,-1,3,2,7,12,-4,0,21,6]
print(bubble_sort(nums))

