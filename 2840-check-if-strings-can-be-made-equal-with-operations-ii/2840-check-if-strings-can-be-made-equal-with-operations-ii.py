from collections import Counter

class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return Counter(s1[0::2]) == Counter(s2[0::2]) and \
               Counter(s1[1::2]) == Counter(s2[1::2])