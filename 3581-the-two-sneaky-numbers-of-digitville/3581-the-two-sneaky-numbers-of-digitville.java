import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        Set<Integer> numberSet = new HashSet<>();
        int[] r = new int[2];
        int j = 0;


        for(int i = 0; i < nums.length; i++){
            if(j>= 2) break;
            if (numberSet.contains(nums[i])){
                r[j] = nums[i];
                j+=1;
            }else{
                numberSet.add(nums[i]);
            }
        }

        return r;
    }
}