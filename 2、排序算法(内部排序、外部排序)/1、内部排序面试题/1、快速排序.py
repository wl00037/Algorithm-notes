#   快速排序
#   思路：
#   1、选择一个目标值，将大于目标值的都放到目标值右侧，小于目标值的都放到目标值左侧，当left和right碰头后就是目标值的位置；
#   2、接着通过递归的方法对目标值左、右两部分数组继续求解；

def quick_sort(nums):
    if len(nums) == 0:
        return nums     #   递归出口
    left = 0
    right = len(nums)-1
    tmp = nums[0]
    while(left < right):        #   这个条件一定要有，因为要走到left==right的时候才会确定本次tmp的真正位置；
        while(nums[right] >= tmp and right>left):
            right -= 1
        nums[left] = nums[right]

        while(nums[left] <= tmp and left<right):
            left += 1
        nums[right] = nums[left]

    #   此时找到tmp合适的地方了
    nums[left] = tmp
    quick_sort(nums[0:left])
    quick_sort(nums[left+1:len(nums)])
    return nums

nums = [10,-1,3,2,7,12,-4,0,21,6]
print(quick_sort(nums))



