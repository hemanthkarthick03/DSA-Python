// LeetCode 3: Longest Substring Without Repeating Characters
// Given a string s, find the length of the longest substring without repeating characters.

import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> charMap = new HashMap<>();
        int maxLength = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            
            if (charMap.containsKey(currentChar) && charMap.get(currentChar) >= left) {
                left = charMap.get(currentChar) + 1;
            }
            
            charMap.put(currentChar, right);
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
    
    public static void main(String[] args) {
        LongestSubstringWithoutRepeatingCharacters solution = new LongestSubstringWithoutRepeatingCharacters();
        
        String[] testCases = {"abcabcbb", "bbbbb", "pwwkew", ""};
        
        for (String test : testCases) {
            System.out.println("\"" + test + "\" -> " + solution.lengthOfLongestSubstring(test));
        }
    }
}