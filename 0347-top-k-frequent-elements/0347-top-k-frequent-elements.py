class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            freq_buckets[freq].append(num)
        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res