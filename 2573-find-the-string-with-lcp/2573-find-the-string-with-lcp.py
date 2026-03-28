class Solution(object):
    def findTheString(self, lcp):
        n = len(lcp)
        res = [0] * n
        char_idx = 1
        
        for i in range(n):
            if res[i] > 0:
                continue
            if char_idx > 26:
                return ""
            
            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = char_idx
            char_idx += 1
            
        word_list = []
        for val in res:
            if val == 0: return ""
            word_list.append(chr(ord('a') + val - 1))
        word = "".join(word_list)
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = 0
                
                if dp[i][j] != lcp[i][j]:
                    return ""
                    
        return word