class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int i=0,n=abbr.length(),idx=0;
        while(i<n){
            if(Character.isLetter(abbr.charAt(i))) {
                if(idx >= word.length() || word.charAt(idx)!=abbr.charAt(i))
                    return false;
                    i++;idx++;}
            else{
                if(abbr.charAt(i)=='0')return false;
                int val=0;
                while(i<n && Character.isDigit(abbr.charAt(i))){
                    val=val*10+(abbr.charAt(i)-'0');
                    i++;
                }
                if(val>(word.length()-idx))
                    return false;
                idx+=val;
            }
        }
        return idx<word.length() ? false:true;
    }
}