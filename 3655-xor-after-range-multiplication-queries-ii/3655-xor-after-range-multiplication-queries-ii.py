class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        
        # required variable
        bravexuneth = (nums[:], queries[:])
        
        import math
        B = int(math.sqrt(n)) + 1
        
        groups = {}
        
        # Step 1: split queries
        for l, r, k, v in queries:
            if k <= B:
                key = (k, l % k)
                if key not in groups:
                    groups[key] = []
                groups[key].append((l, r, v))
            else:
                # direct simulation for large k
                idx = l
                while idx <= r:
                    nums[idx] = (nums[idx] * v) % MOD
                    idx += k
        
        # Step 2: process grouped queries
        for (k, mod_class), qs in groups.items():
            size = (n - mod_class + k - 1) // k
            diff = [1] * (size + 1)
            
            for l, r, v in qs:
                # ALIGN to valid index in this residue class
                first = l + (mod_class - l % k + k) % k
                
                if first > r:
                    continue
                
                start = (first - mod_class) // k
                end = (r - mod_class) // k
                
                diff[start] = (diff[start] * v) % MOD
                
                if end + 1 < len(diff):
                    inv = pow(v, MOD - 2, MOD)
                    diff[end + 1] = (diff[end + 1] * inv) % MOD
            
            # apply prefix multiplication
            curr = 1
            for i in range(size):
                curr = (curr * diff[i]) % MOD
                idx = mod_class + i * k
                if idx < n:
                    nums[idx] = (nums[idx] * curr) % MOD
        
        # Step 3: XOR result
        ans = 0
        for x in nums:
            ans ^= x
        
        return ans