"""
link:   https://leetcode.cn/problems/replace-words/description/?envType=study-plan-v2&envId=bytedance-2023-spring-sprint
Author: hhy
"""

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # sort
        dictionary = sorted(dictionary, key=len)

        sentence_split_list = sentence.split(' ')
        result_list = []
        for i, item in enumerate(sentence_split_list):
            judge = False
            for root in dictionary:
                if root == item[:len(root)]:
                    result_list.append(str(root))
                    judge = True
                    break
            if not judge:
                result_list.append(str(item))
        result = ""
        for item in result_list:
            result += str(item) + ' '
        result = result.strip(' ')

        return result
