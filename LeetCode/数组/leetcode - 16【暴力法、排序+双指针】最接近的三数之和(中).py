#   LeeCode - 16、最接近的三数之和
#   题目：给一个数组nums和一个目标值target，从nums中找到三个整数，这三个整数的和最接近target，返回这三个整数和
#
#   例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#   与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

class Solution(object):
    #   方法一：暴力法
    #   思路：组合所有三个数的情况，得到最接近的值；
    def threeSumClosest_ByForce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        AllArrangeList = []
        closest = float("inf")
        result = []
        for x in range(0,len(nums)-2):
            for y in range(x+1,len(nums)-1):
                for z in range(y+1,len(nums)):
                    AllArrangeList.append([nums[x],nums[y],nums[z]])
        for i in range(0,len(AllArrangeList)-1):
            if  abs(sum(AllArrangeList[i]) - target) < closest:
                closest = sum(AllArrangeList[i])-target
                result = AllArrangeList[i]

        return closest,result

    #   方法一：排序+双指针
    #   思路：
    #       1、先对数组进行排序，使用python自带sort，时间复杂度：O(nlogn);
    #       2、遍历nums，每次遍历的元素就是固定的三个数中的一个，nums[i];
    #       3、再使用双指针，start=i+1,end=len(nums)-1;
    #       4、经过这个流程处理后，就变成了：计算nums[i+1:len(nums)]数组中两个数的和与target-nums[i]最接近的搭配；
    #       5、就类似解答：167题：输入有序数组求两个数之和，只不过把和变成了绝对值；

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = float("inf")
        result_list = []
        nums.sort()     #   先对数组排序
        for i in range(0,len(nums)):
            curr_target = target - nums[i]
            start = i+1
            end = len(nums)-1
            while(start<end):
                curr_Twosum = nums[start] + nums[end]
                if abs(curr_Twosum-curr_target)<result:     #
                    #   如果绝对值小，说明离得更近
                    result_list = [nums[i],nums[start],nums[end]]
                    result = abs(curr_Twosum-curr_target)
                elif curr_Twosum > curr_target:                     #   这个就是有序数组求两个元素和与target的
                    end -= 1
                elif curr_Twosum < curr_target:
                    start += 1
                else:               #       这个else表示如果有组合的sum-target=0，就没必要再进行后续计算了，直接返回就可以了
                    result_list = [nums[i],nums[start],nums[end]]
                    result = 0
                    return result_list,result
        return result_list, result

l = [-1,2,1,-4]
l2= [-1,2,1,-4]
target = 1
closest1,result1 = Solution().threeSumClosest(l,target)
closest2,result2 = Solution().threeSumClosest_ByForce(l2,target)
print(closest1,result1)
print(closest2,result2)


