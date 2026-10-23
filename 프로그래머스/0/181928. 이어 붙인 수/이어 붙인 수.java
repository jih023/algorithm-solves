class Solution {
    public int solution(int[] num_list) {
        String even = "";
        String odd = "";
        
        for (int a : num_list) {
            if (a % 2 == 0) {
                even += String.valueOf(a);
            }
            else {
                odd += String.valueOf(a);
            }
        }
        
        int e = Integer.parseInt(even);
        int o = Integer.parseInt(odd);
        
        return e + o;
    }
}