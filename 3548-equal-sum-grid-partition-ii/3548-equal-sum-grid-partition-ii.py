from collections import defaultdict
import bisect

class Solution(object):
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        
        val_positions = defaultdict(list)
        for r in range(m):
            for c in range(n):
                val_positions[grid[r][c]].append((r, c))
        
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        def exists_in_subgrid(target, r1, r2, c1, c2):
            if target not in val_positions:
                return False
            positions = val_positions[target]
            
            idx = bisect.bisect_left(positions, (r1, -1))
            for i in range(idx, len(positions)):
                r, c = positions[i]
                if r > r2:
                    break
                if c1 <= c <= c2:
                    return True
            return False

        def check(target, r1, r2, c1, c2):
            if target == 0: return True
            if r1 == r2:
                return grid[r1][c1] == target or grid[r1][c2] == target
            if c1 == c2:
                return grid[r1][c1] == target or grid[r2][c1] == target
            return exists_in_subgrid(target, r1, r2, c1, c2)

        curr_top = 0
        for i in range(m - 1):
            curr_top += row_sums[i]
            diff = curr_top - (total_sum - curr_top)
            if diff == 0: return True
            if diff > 0 and check(diff, 0, i, 0, n - 1): return True
            if diff < 0 and check(-diff, i + 1, m - 1, 0, n - 1): return True

        curr_left = 0
        for j in range(n - 1):
            curr_left += col_sums[j]
            diff = curr_left - (total_sum - curr_left)
            if diff == 0: return True
            if diff > 0 and check(diff, 0, m - 1, 0, j): return True
            if diff < 0 and check(-diff, 0, m - 1, j + 1, n - 1): return True
            
        return False