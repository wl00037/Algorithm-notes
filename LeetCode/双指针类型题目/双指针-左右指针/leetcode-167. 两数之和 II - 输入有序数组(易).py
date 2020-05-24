#   167. 两数之和 II - 输入有序数组
#   给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#   函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

#   说明:
#       1、返回的下标值（index1 和 index2）不是从零开始的。
#       2、你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

#   示例：
#   输入: numbers = [2, 7, 11, 15], target = 9
#   输出: [1,2]
#   解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2  (index不是从0开始的)

#   思路：采用左右指针
#       1、如果 numbers[left] + numbers[right] > target，则：right-1，即右指针向左移动一位
#       2、如果numbers[left] + numbers[right] < target，则：left+1，即左指针向右移动一位

class Solution(object):
    def twoSum(self, numbers, target):
        left,right = 0 ,len(numbers)-1
        while(left != right):
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return left+1,right+1
        return 0,0

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    left,right = Solution().twoSum(numbers,target)
    print(left,right)