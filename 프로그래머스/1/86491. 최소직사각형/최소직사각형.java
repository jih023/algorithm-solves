class Solution {
    public int solution(int[][] sizes) {
        int size = sizes.length;
        
        int max_size = 0;
        int min_size = 0;
        
        for (int i = 0; i < size; i++) {
            if (sizes[i][0] >= sizes[i][1]) {
                max_size = Math.max(max_size, sizes[i][0]);
                min_size = Math.max(min_size, sizes[i][1]);
            }
            else if (sizes[i][0] < sizes[i][1]) {
                max_size = Math.max(max_size, sizes[i][1]);
                min_size = Math.max(min_size, sizes[i][0]);
            }
        }
                               
        int answer = max_size * min_size;
        return answer;
    }
}