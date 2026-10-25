import java.util.Arrays;

class Solution {
    public int[] solution(int[] answers) {
        int score1 = 0;
        int score2 = 0;
        int score3 = 0;
        
        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] arr3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int len = answers.length;
        
        for (int i = 0; i < len; i++) {
            int n1 = i % 5;
            int n2 = i % 8;
            int n3 = i % 10;
            
            if (answers[i] == arr1[n1]) {
                score1 += 1;
            }
            if (answers[i] == arr2[n2]) {
                score2 += 1;
            }
            if (answers[i] == arr3[n3]) {
                score3 += 1;
            }
        }
        
        int[] answer = new int[3];
        int idx = 0;
        
        int maxScore = Math.max(score1, Math.max(score2, score3));
        
        if (score1 == maxScore) answer[idx++] = 1;
        if (score2 == maxScore) answer[idx++] = 2;
        if (score3 == maxScore) answer[idx++] = 3;
        
        return Arrays.copyOf(answer, idx);
    }
}