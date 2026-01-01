import java.util.*;

class Permutation {
    public boolean checkInclusion(String s2, String s1) {
        // Frequency arrays for characters in s1 and s2
        int[] s2Freq = new int[26]; // Frequency array for s2
        int[] s1Freq = new int[26]; // Frequency array for current window in s1

        int len1 = s1.length();
        int len2 = s2.length();

        // If s2 is longer than s1, no permutation of s2 can be a substring of s1
        if (len2 > len1)
            return false;

        // Initialize frequency arrays for s2 and the first window in s1
        for (int i = 0; i < len2; i++) {
            s2Freq[s2.charAt(i) - 'a']++;
            s1Freq[s1.charAt(i) - 'a']++;
        }

        // Sliding window to check the remaining windows in s1
        for (int i = len2; i < len1; i++) {
            // If the current window matches the frequency of s2, return true
            if (matches(s2Freq, s1Freq))
                return true;

            // Slide the window: add the new character and remove the old one
            s1Freq[s1.charAt(i) - 'a']++; // Add new character to the window
            s1Freq[s1.charAt(i - len2) - 'a']--; // Remove character that's no longer in the window
        }

        // Check the last window
        return matches(s2Freq, s1Freq);
    }

    // Helper function to compare two frequency arrays
    private boolean matches(int[] s2Freq, int[] s1Freq) {
        for (int i = 0; i < 26; i++) {
            if (s2Freq[i] != s1Freq[i])
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String s1 = "eidbaooo";
        String s2 = "ab";

        System.out.println(sol.checkInclusion(s2, s1)); // Output: true
    }
}
