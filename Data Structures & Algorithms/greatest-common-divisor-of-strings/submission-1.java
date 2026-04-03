class Solution {
    public static int findgcd(int x,int y){
        if (y==0)
            return x;
        return findgcd(y,x%y);
    }
    public String gcdOfStrings(String str1, String str2) {
        int gcd=findgcd(str1.length(),str2.length());
        String res=str1.substring(0,gcd);
        return str1.concat(str2).equals(str2.concat(str1))? res :  "";
    }
}