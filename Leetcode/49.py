"""
Link:   'https://leetcode.cn/problems/group-anagrams/?envType=study-plan-v2&envId=top-100-liked'
Author: hhy-huang
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dictt = defaultdict(list)
        for item in strs:
            dictt["".join(sorted(item))].append(item)
        res = [v for v in dictt.values()]
        return res
