#   冒泡排序
#   思路：
#   外层遍历的索引位置上不断和内层遍历的值比较，保证外层遍历所处的索引位上一定是最小的值；
#   时间复杂度 O(n^2)

def bubble_sort(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                # index-i和后面所有索引位上的值挨个对比，将最小的一个放到index-i上
                array[i],array[j] = array[j],array[i]
    return array

if __name__ == "__main__":
    array = [45,2,61,0,-3,77,13,-53,-23,7]
    print(bubble_sort(array))
