#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<int>
#define vvi vector<vector<int>> // Fixed typo here (missing closing '>')

class Solution {
public:
    int maxWalls(vi& robots, vi& distance, vi& walls) {
        int n = robots.size();
        
        // Pair robots' positions with their corresponding distances
        vector<pair<int, int>> R(n);
        for(int i = 0; i < n; ++i) {
            R[i] = {robots[i], distance[i]};
        }
        sort(R.begin(), R.end()); // Sort robots by position
        
        sort(walls.begin(), walls.end());
        int base_ans = 0;
        vi filtered;
        
        // Walls exactly at a robot's position are guaranteed to be destroyed
        for(int w : walls) {
            auto it = lower_bound(R.begin(), R.end(), make_pair(w, -1));
            if(it != R.end() && it->first == w) {
                base_ans++;
            } else {
                filtered.push_back(w);
            }
        }
        walls = move(filtered);
        
        // Lambda to efficiently count walls enclosed completely within [L, R_val]
        auto count_in = [&](int L, int R_val) -> int {
            if (L > R_val) return 0;
            auto it1 = lower_bound(walls.begin(), walls.end(), L);
            auto it2 = upper_bound(walls.begin(), walls.end(), R_val);
            return it2 - it1;
        };
        
        // Base case: first interval strictly ending before the 0-th robot
        int prev0 = count_in(R[0].first - R[0].second, R[0].first - 1);
        int prev1 = 0;
        
        // DP transitions on adjacent pair independent intervals
        for(int i = 1; i < n; ++i) {
            int X_prev = R[i-1].first, D_prev = R[i-1].second;
            int X_curr = R[i].first, D_curr = R[i].second;
            
            int A_len = count_in(X_prev + 1, X_curr - 1);
            int p = count_in(X_prev + 1, min(X_curr - 1, X_prev + D_prev));
            int s = count_in(max(X_prev + 1, X_curr - D_curr), X_curr - 1);
            
            // curr0: Max unique walls destroyed globally up to interval i given robot i fires Left
            int curr0 = max(prev0 + s, prev1 + min(A_len, p + s));
            
            // curr1: Max unique walls destroyed globally up to interval i given robot i fires Right
            int curr1 = max(prev0, prev1 + p);
            
            prev0 = curr0;
            prev1 = curr1;
        }
        
        // Calculate the last unconstrained interval progressing arbitrarily towards infinity
        int right_count = count_in(R[n-1].first + 1, R[n-1].first + R[n-1].second);
        
        return base_ans + max(prev0, prev1 + right_count);
    }
};