class Solution {
    public static int findgcd(int x,int y){
        if (y==0)
            return x;
        return findgcd(y,x%y);
    }
    public String gcdOfStrings(String str1, String str2) {
        if(!str1.concat(str2).equals(str2.concat(str1)))
            return  "";
        int gcd=findgcd(str1.length(),str2.length());
        return str1.substring(0,gcd) ;
    }
}