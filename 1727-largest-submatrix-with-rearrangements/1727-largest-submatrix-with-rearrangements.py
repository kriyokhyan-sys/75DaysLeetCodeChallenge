class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        
        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]
        
        for r in range(rows):
            current_row = sorted(matrix[r], reverse=True)
            for i in range(cols):
                max_area = max(max_area, current_row[i] * (i + 1))
                
        return max_area