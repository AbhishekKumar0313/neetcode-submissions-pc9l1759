class Solution {

    public String addBinary(String a, String b) {
        int carry = 0;
        StringBuilder res = new StringBuilder();
        int i = a.length() - 1, j = b.length() - 1;
        while (i >= 0 || j >= 0) {
            int x = i >= 0 ? a.charAt(i) - '0' : 0;
            int y = j >= 0 ? b.charAt(j) - '0' : 0;
            System.out.println(x + " " + y + " " + carry);
            int total = x + y + carry;
            res.append(total % 2);
            carry = total / 2;
            i--;
            j--;
        }
        System.out.println(carry);
        if (carry != 0) res.append(carry);
        return res.reverse().toString();
    }
}
