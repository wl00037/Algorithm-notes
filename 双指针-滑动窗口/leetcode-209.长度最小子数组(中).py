#   给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。
#   如果不存在符合条件的连续子数组，返回 0。

#   示例: 
#   输入: s = 7, nums = [2,3,1,2,4,3]
#   输出: 2       --> 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

#   方法一：暴力法
#   思路很简单，组合所有可出现的数组，然后算出来大于t的，并记录最小满足条件的数组长度
def minSubArrayLen_force(nums,t):
    min_array_length = float("inf")
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if sum(nums[i:j+1])>=t and j+1-i<min_array_length:
                min_array_length = j+1-i
    return min_array_length


#   方法二：滑动窗口
#   思路：
#   1、right向右移动，找到nums[left:right+1]>=t而nums[left:right]<t的临界点
#   2、left右移，找到nums[left:right+1]>=t而nums[left+1:right+1]<t的临界点
def minSubArrayLen_SlidingWindow(nums,t):
    min_Array_length = float("inf")
    left = 0
    min_array = []
    for right in range(0,len(nums)):
        if sum(nums[left:right]) < t and sum(nums[left:right+1]):
            #   这个地方有个需要注意的，a[0:0] -> [];sum(a[0:0])->0，所以这个地方只能用：sum(nums[left:right]) < t and sum(nums[left:right+1])判断；
            if right+1-left < min_Array_length:     #   先判断并记录本次子数组的长度和内容
                min_Array_length = right+1-left
                min_array = nums[left:right+1]
            while (left <= right):
                if sum(nums[left:right+1]) >= t:
                    min_Array_length = right + 1 - left
                    min_array = nums[left:right + 1]
                    left += 1
                    continue
                left+=1
                break
    if min_Array_length == float("inf"):        #   满足题目条件，无大于t的子数组返回0
        min_Array_length = 0
    return min_Array_length
