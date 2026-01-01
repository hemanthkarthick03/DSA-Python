// LeetCode 191: Number of 1 Bits
// Write a function that takes an unsigned integer and returns the number of '1' bits it has.

public class NumberOfOneBits {
    public int hammingWeight(int n) {
        int count = 0;
        
        while (n != 0) {
            count++;
            n &= (n - 1); // Remove the rightmost 1 bit
        }
        
        return count;
    }
    
    // Alternative approach using built-in method
    public int hammingWeightBuiltIn(int n) {
        return Integer.bitCount(n);
    }
    
    // Alternative approach using bit shifting
    public int hammingWeightShift(int n) {
        int count = 0;
        
        while (n != 0) {
            count += n & 1;
            n >>>= 1; // Unsigned right shift
        }
        
        return count;
    }
    
    public static void main(String[] args) {
        NumberOfOneBits solution = new NumberOfOneBits();
        int n1 = 11; // Binary: 1011
        int n2 = 128; // Binary: 10000000
        
        System.out.println("Number of 1 bits in " + n1 + ": " + solution.hammingWeight(n1));
        System.out.println("Number of 1 bits in " + n2 + ": " + solution.hammingWeight(n2));
    }
}