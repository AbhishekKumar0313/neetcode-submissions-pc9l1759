class Solution {
    public int[] singleNumber(int[] nums) {
         //find xor of those two unique number
        int xor = 0;
        for (int ele : nums) {
            xor ^= ele;
        }
        // find set bit position in the xor
        int pos = 0;
        while (xor != 0) {
            if ((xor & 1) != 0) break;
            xor = xor >> 1;
            pos += 1;
        }
        // make two variable that manage two category of elements in array
        int zero = 0, one = 0;
        for (int ele : nums) {
            if ((ele & (1 << pos)) == 0) zero ^= ele; else {
                one ^= ele;
            }
        }
        return new int[] { zero, one };
        
    }
}