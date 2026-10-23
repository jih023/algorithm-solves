class Solution {
    public int solution(int[] num_list) {
        int n = num_list.length;
        for (int i = 0; i < n; i++) {
            if (num_list[i] < 0) {
                return i;
            }
        }
        return -1;
    }
}