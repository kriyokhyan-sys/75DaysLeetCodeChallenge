import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minMirrorPairDistance(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int minDistance = Integer.MAX_VALUE;
        boolean found = false;

        for (int j = 0; j < nums.length; j++) {
            // Check if any previous nums[i] had a reverse equal to the current nums[j]
            if (map.containsKey(nums[j])) {
                minDistance = Math.min(minDistance, j - map.get(nums[j]));
                found = true;
            }

            // Store the reverse of the current number as the key
            // This allows a future nums[k] to match if nums[k] == reverse(nums[j])
            int rev = reverse(nums[j]);
            map.put(rev, j);
        }

        return found ? minDistance : -1;
    }

    private int reverse(int n) {
        int rev = 0;
        while (n > 0) {
            rev = rev * 10 + (n % 10);
            n /= 10;
        }
        return rev;
    }
}