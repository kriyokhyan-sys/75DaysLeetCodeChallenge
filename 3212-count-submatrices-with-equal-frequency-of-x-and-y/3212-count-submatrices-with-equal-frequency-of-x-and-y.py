class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        prefix_x = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefix_y = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                val_x = 1 if grid[r][c] == 'X' else 0
                val_y = 1 if grid[r][c] == 'Y' else 0
                
                prefix_x[r+1][c+1] = val_x + prefix_x[r][c+1] + prefix_x[r+1][c] - prefix_x[r][c]
                prefix_y[r+1][c+1] = val_y + prefix_y[r][c+1] + prefix_y[r+1][c] - prefix_y[r][c]
                
                curr_x = prefix_x[r+1][c+1]
                curr_y = prefix_y[r+1][c+1]
                
                if curr_x > 0 and curr_x == curr_y:
                    count += 1
                    
        return count