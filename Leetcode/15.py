"""
Link:       https://leetcode.cn/problems/3sum/description/?envType=study-plan-v2&envId=top-100-liked
Author:     hhy
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """TLE
        self.res = []
        nums_dict = {}
        set_list = []
        for i, item in enumerate(nums):
            nums_dict[item] = i
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp = -1 * (nums[i] + nums[j])
                if temp in nums_dict.keys():
                    if nums_dict[temp] != i and nums_dict[temp] != j:
                        if set([nums[i], nums[j], temp]) not in set_list:
                            set_list.append(set([nums[i], nums[j], temp]))
                            self.res.append([nums[i], nums[j], temp])"""
        self.res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    self.res.append([nums[i], nums[l], nums[r]])
                    # same item
                    l += 1
                    while l + 1 < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while r - 1 > 0 and nums[r] == nums[r + 1]:
                        r -= 1

        return self.res
