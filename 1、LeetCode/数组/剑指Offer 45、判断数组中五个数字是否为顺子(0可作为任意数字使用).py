#   剑指 Offer 45

#   /*
#   LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
#   他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
#   “红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,
#   并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
#   LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组
#   成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
#   */

#   面试公司：小米金融

#   看题目废话一堆，实际上就是：从四组 1~13 + 4个0 中随机取出45个数，查看是否可以组成顺子，0可以作为任何数字使用

import random

class Solution:
    def IsContinuous(self, numbers):
        numbers.sort()      #   排序
        zero_count = 0      #   0出现的次数

        for i in range(0,5):    #   为了过滤出0出现的次数
            if numbers[i] == 0:
                zero_count += 1
                continue
        No_zero_list = numbers[zero_count:]
        if len(set(No_zero_list)) != 5-zero_count:
            print("出现不同花色的重复牌，无法组成顺子")
            return  False

        differencevalue = max(No_zero_list) - min(No_zero_list) - 1 - (len(No_zero_list) - 2) - zero_count

        if differencevalue == 0:
            print("可以组成顺子")
            return True
        print("无法组成顺子")
        return False

    def SimulationLicensing(self):
        #   模拟：随机抽牌的方法
        #   方法一：使用random.shuffle() 直接将数组打乱，然后取[0,5]
        #   方法二：使用random.choice() 循环五次每次随机选取一个数，这个方法取要将取除的数从数组中删除

        new_list = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4
        new_list.extend([0,0,0,0])
        mychoice = []
        count = 5
        while count > 0 :
            number = random.choice(new_list)
            mychoice.append(number)
            new_list.remove(number)     # 将抽出的数字number从new_list中删除
            count -= 1
        print("随机抽取的牌为：",mychoice)
        return mychoice

s = Solution()
result = s.IsContinuous(s.SimulationLicensing())
print( result)






