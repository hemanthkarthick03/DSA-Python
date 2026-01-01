// LeetCode 125: Valid Palindrome
// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            
            left++;
            right--;
        }
        
        return true;
    }
    
    // Alternative approach using StringBuilder
    public boolean isPalindromeStringBuilder(String s) {
        StringBuilder cleaned = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                cleaned.append(Character.toLowerCase(c));
            }
        }
        
        String cleanedStr = cleaned.toString();
        String reversed = cleaned.reverse().toString();
        
        return cleanedStr.equals(reversed);
    }
    
    public static void main(String[] args) {
        ValidPalindrome solution = new ValidPalindrome();
        
        String[] testCases = {
            "A man, a plan, a canal: Panama",
            "race a car",
            " ",
            "Madam"
        };
        
        for (String test : testCases) {
            System.out.println("\"" + test + "\" is palindrome: " + solution.isPalindrome(test));
        }
    }
}