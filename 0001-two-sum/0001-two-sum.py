class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map={}
        for i,num in enumerate(nums):
            com=target-num
            if com in num_map:
                return [num_map[com],i]
            num_map[num]=i
        
        
        