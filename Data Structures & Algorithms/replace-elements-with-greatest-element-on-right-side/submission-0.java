class Solution {

    public int[] replaceElements(int[] arr) {
        int max_ele = -1;
        for (int i = arr.length - 1; i >= 0; i--) {
            int temp = arr[i];
            arr[i] = max_ele;
            max_ele = Math.max(max_ele, temp);
        }
        return arr;
    }
}
