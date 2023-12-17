"""
link:   https://leetcode.cn/problems/path-with-minimum-effort/description/?envType=study-plan-v2&envId=bytedance-2023-spring-sprint
author: hhy
"""
class Solution(object):
    def __init__(self):
        self.visited = []
        self.m = 0
        self.n = 0

    def dfs(self, cur_x, cur_y, effort, heights):
        if cur_x == self.m - 1 and cur_y == self.n - 1:       # over!
            return True
        self.visited[cur_x][cur_y] = True

        del_x = [-1, 1, 0, 0]
        del_y = [0, 0, -1, 1]
        for i in range(4):
            new_x = cur_x + del_x[i]
            new_y = cur_y + del_y[i]
            if new_x >= 0 and new_x < self.m and new_y >= 0 and new_y < self.n and  not self.visited[new_x][new_y]:
                if abs(heights[new_x][new_y] - heights[cur_x][cur_y]) > effort:
                    continue
                if self.dfs(new_x, new_y, effort, heights):
                    return True
        return False

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        self.m = len(heights)
        self.n = len(heights[0])
        
        left = 0
        right = 1000000
        # 将最值问题转换为二分查找问题
        while left < right:
            mid = (left + right) >> 1
            self.visited = [[0 for _ in range(self.n)] for _ in range(self.m)]
            if not self.dfs(0, 0, mid, heights):
                left = mid + 1
            else:
                right = mid
        return left



        


        
        
