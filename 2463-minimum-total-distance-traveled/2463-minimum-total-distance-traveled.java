import java.util.*;

class Solution {
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        Collections.sort(robot);
        Arrays.sort(factory, (a, b) -> Integer.compare(a[0], b[0]));

        List<Integer> factoryPositions = new ArrayList<>();
        for (int[] f : factory) {
            for (int i = 0; i < f[1]; i++) {
                factoryPositions.add(f[0]);
            }
        }

        int n = robot.size();
        int m = factoryPositions.size();
        long[][] dp = new long[n + 1][m + 1];
        
        for (int i = 1; i <= n; i++) {
            dp[i][0] = (long) 1e15;
        }

        for (int j = 1; j <= m; j++) {
            for (int i = 1; i <= n; i++) {
                long skip = dp[i][j - 1];
                long use = dp[i - 1][j - 1] + Math.abs(robot.get(i - 1) - factoryPositions.get(j - 1));
                dp[i][j] = Math.min(skip, use);
            }
        }

        return dp[n][m];
    }
}