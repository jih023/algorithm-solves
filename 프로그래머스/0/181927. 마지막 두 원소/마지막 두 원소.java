import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int[] answer = Arrays.copyOf(num_list, n + 1);
        
        if (answer[n-1] > answer[n-2]) {
            answer[n] = answer[n-1] - answer[n-2];
        }
        else {
            answer[n] = answer[n-1] * 2;
        }
        
        return answer;
    }
}