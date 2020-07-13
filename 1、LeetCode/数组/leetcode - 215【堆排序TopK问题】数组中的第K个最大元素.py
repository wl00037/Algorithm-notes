#   在未排序的数组中找到第k个最大的元素。
#   请注意，你需要找的是数组排序后的第k个最大的元素，而不是第k个不同的元素。

#   示例 1:
#   输入: [3,2,1,5,6,4] 和 k = 2
#   输出: 5

class Solution(object):

    #   小顶堆概念：任一非终端节点的数据值均不大于其左子节点和右子节点的值，也就是只要是有子节点，那么这个节点一定小于子节点，也就是说越大的值越在下面；

    #   思路：
    #       1、对nums的前k个元素构建一个大小为k的小顶堆；
    #       2、遍历k后面的元素，如果遍历的元素大于nums[0]，那么就将该元素与nums[0]交换，并且重排这个小顶堆；
    #       3、也就是说，永远保证小顶堆中的k个元素是已经遍历过的元素中最大的k个，当元素遍历结束，则小顶堆堆顶就是第k大的元素；

    #   时间按复杂度：O(n+klogk) -> klogk就是堆排序的时间复杂度

    def findKthLargest(self, nums, k):
        self.heapSort(nums,k)       # 先进性一次k大小的小顶堆的初始化；
        for i in range(k,len(nums)):
            if nums[0] < nums[i]:
                nums[0],nums[i] = nums[i],nums[0]       #   当遍历元素大于小顶堆堆顶，则交换后再次对小顶堆排序
                self.heapSort(nums,k)
            else:
                continue
        return  nums[0]

    def heapSort(self,nums,k):
        #   小顶堆就是：(根、非叶子)节点永远小于它的子节点；
        #   注意，传入的k是个数，索引位实际上是 [0~k-1]闭集；

        #   然后从堆顶向下推
        for root in range(0,k):
            left = root * 2 +1
            right = root * 2 +1
            if

                https: // www.zhihu.com / question / 62374994

