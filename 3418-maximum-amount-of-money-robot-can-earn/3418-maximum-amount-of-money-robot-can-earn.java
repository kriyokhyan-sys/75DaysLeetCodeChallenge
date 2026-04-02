class Solution {
    public int maximumAmount(int[][] coins) {
        int m = coins.length;
        int n = coins[0].length;
        int[][][] dp = new int[m][n][3];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < 3; k++) {
                    dp[i][j][k] = Integer.MIN_VALUE;
                }
            }
        }

        dp[0][0][0] = coins[0][0];
        if (coins[0][0] < 0) {
            dp[0][0][1] = 0;
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < 3; k++) {
                    if (dp[i][j][k] == Integer.MIN_VALUE) continue;

                    int[] dr = {0, 1};
                    int[] dc = {1, 0};

                    for (int d = 0; d < 2; d++) {
                        int ni = i + dr[d];
                        int nj = j + dc[d];

                        if (ni < m && nj < n) {
                            dp[ni][nj][k] = Math.max(dp[ni][nj][k], dp[i][j][k] + coins[ni][nj]);

                            if (k < 2 && coins[ni][nj] < 0) {
                                dp[ni][nj][k + 1] = Math.max(dp[ni][nj][k + 1], dp[i][j][k]);
                            }
                        }
                    }
                }
            }
        }

        int result = dp[m - 1][n - 1][0];
        result = Math.max(result, dp[m - 1][n - 1][1]);
        result = Math.max(result, dp[m - 1][n - 1][2]);
        return result;
    }
}