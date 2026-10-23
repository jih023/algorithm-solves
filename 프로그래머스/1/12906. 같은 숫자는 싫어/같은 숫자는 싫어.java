import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int size = arr.length;
        
        int[] answer = new int[size];
        answer[0] = arr[0];
        int idx = 1;
        
        for (int i = 1; i < size; i++) {
            if (answer[idx - 1] != arr[i]) {
                answer[idx] = arr[i];
                idx += 1;
            }
        }

        return Arrays.copyOf(answer, idx);
    }
}