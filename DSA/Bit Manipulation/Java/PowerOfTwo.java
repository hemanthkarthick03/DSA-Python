// LeetCode 231: Power of Two
// Given an integer n, return true if it is a power of two. Otherwise, return false.

public class PowerOfTwo {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        
        // A power of two has exactly one bit set
        // n & (n - 1) removes the rightmost set bit
        // If n is a power of two, this operation results in 0
        return (n & (n - 1)) == 0;
    }
    
    // Alternative approach using bit count
    public boolean isPowerOfTwoBitCount(int n) {
        if (n <= 0) {
            return false;
        }
        
        return Integer.bitCount(n) == 1;
    }
    
    // Alternative approach using logarithm
    public boolean isPowerOfTwoLog(int n) {
        if (n <= 0) {
            return false;
        }
        
        double log = Math.log(n) / Math.log(2);
        return log == Math.floor(log);
    }
    
    public static void main(String[] args) {
        PowerOfTwo solution = new PowerOfTwo();
        int[] testCases = {1, 16, 3, 4, 5, 8};
        
        for (int n : testCases) {
            System.out.println(n + " is power of two: " + solution.isPowerOfTwo(n));
        }
    }
}