class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        int n = encodedText.length();
        if (n == 0) return "";
        
        int cols = n / rows;
        StringBuilder sb = new StringBuilder();
        
        for (int c = 0; c < cols; c++) {
            for (int r = 0; r < rows && (c + r) < cols; r++) {
                int index = r * cols + (c + r);
                sb.append(encodedText.charAt(index));
            }
        }
        
        int lastChar = sb.length() - 1;
        while (lastChar >= 0 && sb.charAt(lastChar) == ' ') {
            lastChar--;
        }
        
        return sb.substring(0, lastChar + 1);
    }
}