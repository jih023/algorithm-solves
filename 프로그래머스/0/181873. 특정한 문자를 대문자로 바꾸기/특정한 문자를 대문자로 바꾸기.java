class Solution {
    public String solution(String my_string, String alp) {
        String answer = "";
    
        int size = my_string.length();
        
        for (int i = 0; i < size; i++) {
            String s = String.valueOf(my_string.charAt(i));
            
            if (s.equals(alp)) {
                answer += s.toUpperCase();
            }
            else {
                answer += s;
            }
        }
        return answer;
    }
}