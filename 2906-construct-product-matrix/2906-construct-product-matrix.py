class Solution(object):
    def constructProductMatrix(self, grid):
        n, m = len(grid), len(grid[0])
        MOD = 12345
        p = [[1] * m for _ in range(n)]
        
        current_product = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = current_product
                current_product = (current_product * grid[i][j]) % MOD
        
        current_product = 1
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                p[i][j] = (p[i][j] * current_product) % MOD
                current_product = (current_product * grid[i][j]) % MOD
                
        return p