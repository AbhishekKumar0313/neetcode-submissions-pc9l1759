class Solution {
    public boolean validWordSquare(List<String> words) {
        int n=words.size();
        for(int i=0;i<n;i++){
            String row=words.get(i);
            for(int j=0;j<row.length();j++){
                if(j>=n) return false;
                if(i>=words.get(j).length())    return false;
                if(row.charAt(j)!=words.get(j).charAt(i))
                    return false;
            }
        }
        return true;
        
    }
}
