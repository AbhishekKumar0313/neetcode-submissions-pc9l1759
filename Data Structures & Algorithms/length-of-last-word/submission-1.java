class Solution {
        public int lengthOfLastWord(String s) {
                int idx=s.length()-1;
                        while(s.charAt(idx)==' '){
                                    idx--;
                                            }
                                                    int length=0;
                                                            while(idx>=0 && s.charAt(idx)!=' '){
                                                                        length++;
                                                                                    idx--;
                                                                                            }
                                                                                                    return length;
                                                                                                        }
                                                                                                        }
