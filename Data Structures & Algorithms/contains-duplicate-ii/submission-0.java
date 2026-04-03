class Solution {

    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int n = nums.length;
        int i = 0, j = 0;
        Set<Integer> set = new HashSet<>();
        while (j < n) {
            set.add(nums[j]);
            if (set.size() < (j - i + 1)) return true;
            if (set.size() == (k + 1)) {
                set.remove(nums[i]);
                i++;
            }
            j++;
        }
        return false;
    }
}