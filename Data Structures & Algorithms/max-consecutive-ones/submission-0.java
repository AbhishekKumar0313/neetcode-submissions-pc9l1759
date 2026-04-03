class Solution {

    public int findMaxConsecutiveOnes(int[] nums) {
        int ones = 0, max_ones = 0;
        for (int ele : nums) {
            ones = ele == 0 ? 0 : ones + 1;
            max_ones = Math.max(ones, max_ones);
        }
        return max_ones;
    }
}
