#   在未排序的数组中找到第k个最大的元素。
#   请注意，你需要找的是数组排序后的第k个最大的元素，而不是第k个不同的元素。

#   示例 1:
#   输入: [3,2,1,5,6,4] 和 k = 2
#   输出: 5

#   本题有两种做法，简单的有直接将数组快排后拿到，本题采用了小顶堆的方式，除了可以拿到第K大的数，同时可以拿到前K大的所有数；


class Solution(object):

    #   小顶堆概念：任一非终端节点的数据值均不大于其左子节点和右子节点的值，也就是只要是有子节点，那么这个节点一定小于子节点，也就是说越大的值越在下面；

    #   思路：
    #       1、对nums的前k个元素初始化构建一个大小为k的小顶堆；
    #       2、遍历k后面的元素，如果遍历的元素大于nums[0]，那么就将该元素与nums[0]交换，并且重排这个小顶堆；

    #   时间按复杂度：O(n+klogk) -> klogk就是堆排序的时间复杂度

    def findKthLargest(self, nums, k):
        self.buildHeap(nums,k)
        len_nums = len(nums)
        for i in range(k,len_nums):
            if nums[i] > nums[0]:
                nums[i],nums[0] = nums[0],nums[i]
                self.heapSort(nums,0,k)
        return nums[0]

    def buildHeap(self,nums,k):
        """
            buildHeap方法用于首次构造nums中前k个元素为小顶堆；
            @param nums：待调整的堆；
            @param k：前k个元素构造小顶堆
        """
        # 首次初始化堆不能从上到下进行，而需要从最后一个拥有子节点的节点逐个向前进行调整，从而保证最小的元素值出现在小顶堆顶
        lastHaveChildNode = (k-1)//2 if k % 2 == 0 else (k-2)//2
        for i in range(lastHaveChildNode,-1,-1):
            self.heapSort(nums,i,k)   #   参数root是索引位，所以一定要 -1

    def heapSort(self,nums,root,k):
        """
            heapSort方法：对堆进行调整
            @param nums：待调整的堆；
            @param root：本次要处理的节点的索引
            @param k：堆的有效大小
        """
        minimum = root  # minimum保存的是root、left、right三个元素中，值最小的元素的索引位
        leftChildIndex = root * 2 + 1
        rightChildIndex = root * 2 + 2
        #   < k的判断是为了保证子节点必须在堆内
        if leftChildIndex < k and nums[leftChildIndex] < nums[minimum]:
            minimum = leftChildIndex
        if rightChildIndex < k and nums[rightChildIndex] < nums[minimum]:
            minimum = rightChildIndex
        #   经过两次if判断，此时的largest就是root和其左右子节点中值最大的元素的索引；

        if minimum != root:
            #   如果传入的根节点不是最小的，那么root、left、right之间就要进行一次交换
            #   当递归到没有子节点的时候，minimium==root，递归不再发生，结束
            nums[root],nums[minimum] = nums[minimum],nums[root]
            self.heapSort(nums,minimum,k)

c = [7,6,5,4,3,2,1]
result = Solution().findKthLargest(c,5)
print(result)
