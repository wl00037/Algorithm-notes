#   LeeCode - 15、三数之和
#   题目：给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 请你找出所有满足条件且不重复的三元组。
#   注意：
#   1、要求就是计算target=0的组合；
#   2、答案中不可以包含重复的三元组；

#   示例：
#   给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#   满足要求的三元组集合为：
#   [
#       [-1, 0, 1],
#       [-1, -1, 2]
#   ]


class Solution(object):

    #   方法一：暴力法
    #   思路：
    #   1、求出来所有的组合，然后去重，然后计算sum是否为0，如果是的话将该数组作为元素放到result数组中；
    #   2、关于不重复：将所有组合全部都按照从小到大排列，那么用 not in 就可以判断是否在result中；
    def threeSum_ByForce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for x in range(0,len(nums)-2):
            for y in range(x+1,len(nums)-1):
                for z in range(y+1,len(nums)):
                    curr_list = [nums[x],nums[y],nums[z]]
                    curr_list.sort()
                    if sum(curr_list) == 0 and curr_list not in result:
                        result.append(curr_list)
        return  result

    #   方法二：排序+双指针      【leetcode上运行超时】
    #   思路：
    #   1、对nums排序
    #   2、每一个nums[i]独立出来，start=i+1，end=len(nums)-1，用nums[start[[+nums[end]的和来判断是否等于 -nums[i]
    #   3、第二步就变成了167题的解题流程
    def threeSum_ByTwoPoint(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(0,len(nums)):
            start = i+1
            end = len(nums)-1
            current = nums[i]
            target = -current
            while(start < end):
                if nums[start] + nums[end] == target and [nums[i],nums[start],nums[end]] not in result:
                    result.append([nums[i],nums[start],nums[end]])
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
        return  result

    #   方法三：排序+双指针的优化     ------【相当坑的一道题】
    #   思考：方法二中是否存在不必要的遍历、循环和判断？
    #
    #   ⭐优化点1：本题目条件a+b+c=0，并且我们对nums进行了排序，当nums[i]>0，则表示i之后所有元素均大于0，三个大于0的数相加不可能为0，所以没必要再遍历；
    #   ⭐优化点2：如果nums[i] = nums[i+1]，其实也没有必要再对i+1进行一次处理，可以直接过滤掉；
    #   ⭐优化点3：如果strat和start+1的值一样，那么这个start+1也没有必要再计算一次，可以直接过滤掉，end同理；

    #   优化过程中的坑：
    #   1、遍历过程中过滤连续两个相同的nums[i]时要考虑[0,0,0]的情况，所以不选择if nums[i] == nums[i+1]，而选择if i>0 and nums[i] == nums[i-1]
    #   2、nums[start]与nums[start-1]以及nums[end] == nums[end+1]的判断的地点要注意，要放在找到a+b+c=0的组合时就进行判断，否则可能出现连续两个组合相同并都进行了添加的情况，比如 [-2,0,0,2,2]
    def threeSum_ByTwoPointOptimize(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:    #如果没有i>0，第一个就会报错，i-1超出范围。
                continue
            start = i+1
            end = len(nums)-1
            target = -nums[i]
            while(start < end):
                if nums[start] + nums[end] == target:
                    result.append([nums[i],nums[start],nums[end]])
                    start += 1
                    end -= 1
                    while(nums[start] == nums[start-1] and start < end):
                        start += 1
                    while(nums[end] == nums[end+1] and end > start):
                        end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
        return  result

nums = [0,0,0]
res = Solution().threeSum_ByForce(nums)
res2 = Solution().threeSum_ByTwoPoint(nums)
res3 = Solution().threeSum_ByTwoPointOptimize(nums)
print(res)
print(res2)
print(res3)
