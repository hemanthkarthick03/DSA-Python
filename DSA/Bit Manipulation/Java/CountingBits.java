// LeetCode 338: Counting Bits
// Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

public class CountingBits {
    public int[] countBits(int n) {
        int[] result = new int[n + 1];
        
        for (int i = 1; i <= n; i++) {
            // i & (i - 1) removes the rightmost 1 bit
            // So count[i] = count[i & (i - 1)] + 1
            result[i] = result[i & (i - 1)] + 1;
        }
        
        return result;
    }
    
    // Alternative DP approach
    public int[] countBitsDP(int n) {
        int[] result = new int[n + 1];
        
        for (int i = 1; i <= n; i++) {
            // If i is even: count[i] = count[i/2]
            // If i is odd: count[i] = count[i/2] + 1
            result[i] = result[i >> 1] + (i & 1);
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        CountingBits solution = new CountingBits();
        int n = 5;
        
        int[] result = solution.countBits(n);
        System.out.print("Counting bits for 0 to " + n + ": [");
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + (i < result.length - 1 ? ", " : ""));
        }
        System.out.println("]");
    }
}