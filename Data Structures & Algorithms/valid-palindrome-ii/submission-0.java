class Solution {

    // will check if valid or not
    public boolean HelperFunction(int i, int j, String str) {
        while (i < j) {
            if (str.charAt(i) != str.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }

    public boolean validPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                if (HelperFunction(left + 1, right, s) || HelperFunction(left, right - 1, s)) return true;
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
