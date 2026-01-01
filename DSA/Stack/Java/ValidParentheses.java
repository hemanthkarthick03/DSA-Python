// LeetCode 20: Valid Parentheses
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

import java.util.Stack;
import java.util.HashMap;
import java.util.Map;

public class ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');
        
        for (char c : s.toCharArray()) {
            if (mapping.containsKey(c)) {
                // Closing bracket
                char topElement = stack.empty() ? '#' : stack.pop();
                if (topElement != mapping.get(c)) {
                    return false;
                }
            } else {
                // Opening bracket
                stack.push(c);
            }
        }
        
        return stack.isEmpty();
    }
    
    public static void main(String[] args) {
        ValidParentheses solution = new ValidParentheses();
        String[] testCases = {"()", "()[]{}", "(]", "([)]", "{[]}"};
        
        for (String test : testCases) {
            System.out.println("\"" + test + "\" is valid: " + solution.isValid(test));
        }
    }
}