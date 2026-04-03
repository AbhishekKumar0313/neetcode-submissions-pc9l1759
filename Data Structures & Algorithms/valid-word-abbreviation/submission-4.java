class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int i=0,n=abbr.length(),idx=0;
        while(i<n){
            if(Character.isLetter(abbr.charAt(i))) {
                if(idx >= word.length() || word.charAt(idx)!=abbr.charAt(i))
                    return false;
                    i++;idx++;}
            else{
                StringBuilder sb=new StringBuilder();
                if(abbr.charAt(i)=='0')return false;
                while(i<n && Character.isDigit(abbr.charAt(i))){
                    sb.append(abbr.charAt(i));
                    i++;
                }
                int val=Integer.valueOf(sb.toString());
                if(val>(word.length()-idx))
                    return false;
                idx+=val;
                System.out.println(i+" "+idx);
            }
        }
        return idx<word.length() ? false:true;
    }
}