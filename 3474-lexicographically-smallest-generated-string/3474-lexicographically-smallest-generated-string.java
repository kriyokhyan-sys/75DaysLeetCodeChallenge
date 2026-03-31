class Solution {
    public String generateString(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();
        int targetLen = n + m - 1;
        char[] res = new char[targetLen];
        boolean[] fixed = new boolean[targetLen];

        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'T') {
                for (int j = 0; j < m; j++) {
                    if (fixed[i + j] && res[i + j] != str2.charAt(j)) {
                        return "";
                    }
                    res[i + j] = str2.charAt(j);
                    fixed[i + j] = true;
                }
            }
        }

        for (int i = 0; i < targetLen; i++) {
            if (!fixed[i]) {
                for (char c = 'a'; c <= 'z'; c++) {
                    res[i] = c;
                    if (checkValid(res, fixed, i, str1, str2)) {
                        break;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'F' && isMatch(res, i, str2)) {
                return "";
            }
        }

        return new String(res);
    }

    private boolean checkValid(char[] res, boolean[] fixed, int idx, String str1, String str2) {
        int m = str2.length();
        for (int i = Math.max(0, idx - m + 1); i <= Math.min(idx, str1.length() - 1); i++) {
            if (str1.charAt(i) == 'F') {
                if (isFullyDetermined(fixed, i, m, idx)) {
                    if (isMatch(res, i, str2)) return false;
                }
            }
        }
        return true;
    }

    private boolean isFullyDetermined(boolean[] fixed, int start, int m, int currentIdx) {
        for (int j = 0; j < m; j++) {
            int pos = start + j;
            if (!fixed[pos] && pos > currentIdx) return false;
        }
        return true;
    }

    private boolean isMatch(char[] res, int start, String str2) {
        for (int j = 0; j < str2.length(); j++) {
            if (res[start + j] != str2.charAt(j)) return false;
        }
        return true;
    }
}