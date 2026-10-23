import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        int size = s.length();
        
        for (int i = 0; i < size; i++) {
            char str = s.charAt(i);
            if (str == '(') {
                stack.push(str);
            }
            else {
                if (stack.isEmpty()) {
                    return false;
                }
                else {
                    stack.pop();
                }
            }
        }

        return stack.isEmpty();
    }
}