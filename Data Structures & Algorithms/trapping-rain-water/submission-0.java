class Solution {

    public int trap(int[] height) {
        int n = height.length;
        int[] left = new int[n];
        int[] right = new int[n];
        // finding left heights
        int max_height = height[0];
        for (int i = 0; i < n; i++) {
            max_height = Math.max(max_height, height[i]);
            left[i] = max_height;
        }

        // finding right heights
        max_height = height[n - 1];
        for (int i = n - 1; i >= 0; i--) {
            max_height = Math.max(max_height, height[i]);
            right[i] = max_height;
        }

        // finding total logged water blocks
        int water_logged_count = 0;
        for (int i = 1; i < n - 1; i++) {
            water_logged_count += Math.min(left[i], right[i]) - height[i];
        }
        return water_logged_count;
    }
}
