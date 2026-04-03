class Solution {

    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left <= right) {
            while (left < right && !isAlphaNumeric(s.charAt(left))) {
                left++;
            }
            while (right > left && !isAlphaNumeric(s.charAt(right))) {
                right--;
            }
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) return false;

            left++;
            right--;
        }
        return true;
    }

    public static boolean isAlphaNumeric(char c) {
        char ch = Character.toLowerCase(c);
        return (ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9');
    }
    
}
