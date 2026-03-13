import java.util.*;

class Solution {
    public long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {
        long low = 0;
        long high = 10000000000000000L; 
        long ans = high;

        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (canFinish(mountainHeight, workerTimes, mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private boolean canFinish(int mountainHeight, int[] workerTimes, long maxTime) {
        long currentHeightReduced = 0;
        for (int w : workerTimes) {
            long limit = (2 * maxTime) / w;
            long x = (long) ((Math.sqrt(1 + 4 * limit) - 1) / 2);
            currentHeightReduced += x;
            if (currentHeightReduced >= mountainHeight) {
                return true;
            }
        }
        return currentHeightReduced >= mountainHeight;
    }
}