class Solution(object):
    def canPartitionGrid(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        total_sum = sum(sum(row) for row in grid)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        row_prefix_sum = 0
        for r in range(m - 1):
            row_prefix_sum += sum(grid[r])
            if row_prefix_sum == target:
                return True
        
        col_sums = [0] * n
        for r in range(m):
            for c in range(n):
                col_sums[c] += grid[r][c]
                
        col_prefix_sum = 0
        for c in range(n - 1):
            col_prefix_sum += col_sums[c]
            if col_prefix_sum == target:
                return True
                
        return False