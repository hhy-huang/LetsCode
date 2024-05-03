#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        t = 0
        b = m - 1
        l = 0
        r = n - 1
        while True:
            temp1 = []
            for j, i in enumerate(range(l, r + 1)):
                temp1.append(matrix[t][i])
            temp2 = []
            for j, i in enumerate(range(t, b + 1)):
                temp2.append(matrix[i][r])
            temp3 = []
            for j, i in enumerate(range(r, l - 1, -1)):
                temp3.append(matrix[b][i])
            temp4 = []
            for j, i in enumerate(range(b, t - 1, -1)):
                temp4.append(matrix[i][l])

            for j, i in enumerate(range(l, r + 1)):
                matrix[t][i] = temp4[j]
            for j, i in enumerate(range(t, b + 1)):
                matrix[i][r] = temp1[j]
            for j, i in enumerate(range(r, l - 1, -1)):
                matrix[b][i] = temp2[j]
            for j, i in enumerate(range(b, t - 1, -1)):
                matrix[i][l] = temp3[j]
            
            t += 1
            b -= 1
            l += 1
            r -= 1
            if t > b:
                break
            if l > r:
                break
# @lc code=end

