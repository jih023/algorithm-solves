class Solution {
    public int[] solution(int[] num_list, int n) {
        int size = num_list.length;
        int[] answer = new int[(size + n - 1) / n];
        int idx = 0;
        
        for (int i = 0; i < size; i += n) {
            answer[idx++] = num_list[i];
        }
        
        return answer;
    }
}