#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """llist = [0] * 2 * 10**4
        self.res = []
        for item in intervals:
            a = item[0]
            b = item[1]
            llist[a] += 1
            llist[b + 1] -= 1
        lastnum = 0
        curtuple = []
        for i in range(len(llist)):
            if i != 0 :
                llist[i] += llist[i - 1]
            #print(f"i: {i}, val: {llist[i]}")
            if llist[i] !=0 and lastnum == 0:
                curtuple.append(i)
                lastnum = 1
            elif llist[i] == 0 and lastnum == 1:
                curtuple.append(i - 1)
                self.res.append(curtuple)
                curtuple = []
                lastnum = 0"""
        self.res = []
        intervals = sorted(intervals, key=lambda i: i[0])
        for i in intervals:
            if self.res and i[0] <= self.res[-1][1]:
                self.res[-1][1] = max(i[1] ,self.res[-1][1])
            else:
                self.res.append(i)
        return self.res
# @lc code=end

