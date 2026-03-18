class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if r > 0:
                    grid[r][c] += grid[r-1][c]
                if c > 0:
                    grid[r][c] += grid[r][c-1]
                if r > 0 and c > 0:
                    grid[r][c] -= grid[r-1][c-1]
                
                if grid[r][c] <= k:
                    count += 1
                else:
                    break
                    
        return count