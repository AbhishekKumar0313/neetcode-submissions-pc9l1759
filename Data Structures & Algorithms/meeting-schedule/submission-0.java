/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        int [] check=new int[1000001];
        for(Interval x:intervals){
            for(int i=x.start;i<x.end;i++)
            {
                if(check[i]==1)
                return false;
            check[i]=1;
            }
        }
        return true;

    }
}
