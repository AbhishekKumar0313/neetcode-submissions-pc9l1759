class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder res=new StringBuilder();
        while(columnNumber>0){
            // we are taking index 0 - 25 not 1-26
            columnNumber--;
            res.append((char)('A'+(columnNumber%26)));
            columnNumber/=26;
        }
        res.reverse();
        return res.toString();   
    }
}