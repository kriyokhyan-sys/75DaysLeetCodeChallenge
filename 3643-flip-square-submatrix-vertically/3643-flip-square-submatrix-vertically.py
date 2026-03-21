class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range(k // 2):
            top_row = x + i
            bottom_row = x + k - 1 - i
            
            for j in range(y, y + k):
                grid[top_row][j], grid[bottom_row][j] = grid[bottom_row][j], grid[top_row][j]
        
        return grid