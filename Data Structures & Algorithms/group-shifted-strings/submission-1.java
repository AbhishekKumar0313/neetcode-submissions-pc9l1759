class Solution {
    public List<List<String>> groupStrings(String[] strings) {
      Map<String,List<String>> hashmap=new HashMap<>();
        for(String word:strings){
            int [] temp=new int[word.length()-1];
            for(int i=1;i<word.length();i++)
                temp[i-1]=(word.charAt(i)-word.charAt(i-1)+26)%26;
            String key=Arrays.toString(temp);
            hashmap.putIfAbsent(key,new ArrayList<>());
            hashmap.get(key).add(word);
        } 
        return new ArrayList<>(hashmap.values());
    }
}
