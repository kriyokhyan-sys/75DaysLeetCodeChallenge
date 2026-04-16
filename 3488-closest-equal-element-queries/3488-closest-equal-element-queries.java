import java.util.*;

class Solution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        int n = nums.length;
        Map<Integer, List<Integer>> map = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        
        List<Integer> result = new ArrayList<>(queries.length);
        
        for (int targetIdx : queries) {
            int val = nums[targetIdx];
            List<Integer> indices = map.get(val);
            
            if (indices.size() <= 1) {
                result.add(-1);
                continue;
            }
            
            int pos = Collections.binarySearch(indices, targetIdx);
            int minDist = n;
            
            int leftIdx = (pos > 0) ? indices.get(pos - 1) : indices.get(indices.size() - 1);
            minDist = Math.min(minDist, getCircularDist(targetIdx, leftIdx, n));
            
            int rightIdx = (pos < indices.size() - 1) ? indices.get(pos + 1) : indices.get(0);
            minDist = Math.min(minDist, getCircularDist(targetIdx, rightIdx, n));
            
            result.add(minDist);
        }
        
        return result;
    }
    
    private int getCircularDist(int i, int j, int n) {
        int absDist = Math.abs(i - j);
        return Math.min(absDist, n - absDist);
    }
}