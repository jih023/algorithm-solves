class Solution {
    public int[] solution(int brown, int yellow) {
        for (int y = 1; y * y <= yellow; y++) {
            if (yellow % y == 0) {
                int x = yellow / y;
                if (y * 2 + x * 2 + 4 == brown) {
                    return new int[]{x + 2, y + 2};
                }
            }
        }
        
        return new int[]{0, 0};
    }
}