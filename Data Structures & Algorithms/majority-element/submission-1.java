class Solution {

    public int majorityElement(int[] nums) {
        int count = 0, candidate = 0;
        for (int cand : nums) {
            if (count == 0) candidate = cand;
            if (cand == candidate) {
                count++;
            } else {
                count--;
            }
        }
        System.out.println(candidate);
        int freq = 0;
        for (int ele : nums) {
            if (ele == candidate) freq++;
        }
        return freq > nums.length / 2 ? candidate : -1;
    }
}
