import java.util.*;

class Solution {
    public int minimumDistance(int[] nums) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }

        int minDistance = Integer.MAX_VALUE;
        boolean found = false;

        for (List<Integer> indices : map.values()) {
            if (indices.size() >= 3) {
                found = true;
                for (int i = 0; i <= indices.size() - 3; i++) {
                    int distance = 2 * (indices.get(i + 2) - indices.get(i));
                    minDistance = Math.min(minDistance, distance);
                }
            }
        }

        return found ? minDistance : -1;
    }
}