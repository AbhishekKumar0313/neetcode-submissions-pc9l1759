class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int ones=0,maxones=0;
        for(int ele : nums){
            if(ele==1)
                ones++;
            else{
                maxones=Math.max(ones,maxones);
                ones=0;
            }
        }
        return Math.max(maxones,ones);   
    }
}