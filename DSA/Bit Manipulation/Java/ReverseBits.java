// LeetCode 190: Reverse Bits
// Reverse bits of a given 32 bits unsigned integer.

public class ReverseBits {
    public int reverseBits(int n) {
        int result = 0;
        
        for (int i = 0; i < 32; i++) {
            result <<= 1; // Shift result left by 1
            result |= (n & 1); // Add the least significant bit of n
            n >>= 1; // Shift n right by 1
        }
        
        return result;
    }
    
    // Alternative approach using bit manipulation tricks
    public int reverseBitsOptimized(int n) {
        // Swap adjacent bits
        n = ((n & 0xaaaaaaaa) >>> 1) | ((n & 0x55555555) << 1);
        // Swap adjacent pairs
        n = ((n & 0xcccccccc) >>> 2) | ((n & 0x33333333) << 2);
        // Swap adjacent nibbles
        n = ((n & 0xf0f0f0f0) >>> 4) | ((n & 0x0f0f0f0f) << 4);
        // Swap adjacent bytes
        n = ((n & 0xff00ff00) >>> 8) | ((n & 0x00ff00ff) << 8);
        // Swap adjacent 16-bit blocks
        n = (n >>> 16) | (n << 16);
        
        return n;
    }
    
    public static void main(String[] args) {
        ReverseBits solution = new ReverseBits();
        int n = 43261596; // Binary: 00000010100101000001111010011100
        
        int reversed = solution.reverseBits(n);
        System.out.println("Original: " + Integer.toBinaryString(n));
        System.out.println("Reversed: " + Integer.toBinaryString(reversed));
        System.out.println("Reversed value: " + reversed);
    }
}