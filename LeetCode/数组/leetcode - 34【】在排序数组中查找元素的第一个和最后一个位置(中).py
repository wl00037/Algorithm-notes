#   给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#   你的算法时间复杂度必须是O(logn)级别。
#   如果数组中不存在目标值，返回 [-1, -1]。

class Solution(object):
    #   要求：logn的时间复杂度 -> 看到logn我们就应该想到：二分法
    #   思路：二分法找到target，然后向两边扩展，找到不第一个和最后一个地址；
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right = 0,len(nums)
        while left < right:
            mid = left + (right - left) // 2        #   这个地方用 mid = left + (right - left) // 2 比较好
            mid = (left + right ) //2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:       #   nums[mid] == target
                result_left,result_right = mid,mid
                while result_left > 0 and nums[result_left-1] == target:
                    result_left -= 1
                while result_right < len(nums)-1 and nums[result_right+1] == target:
                    result_right += 1
                return [result_left,result_right]
        return  [-1,-1]


l = [1]
l2 = [5,7,7,8,8,10]
target = 1
result = Solution().searchRange(l,target)
print(result)

