class Solution {
    public int differenceOfSum(int[] nums) {

        int sums = 0;
        int digitSum = 0;

        for(int i = 0; i < nums.length; i++){
            int val = nums[i];
            sums+= val;
            while (val > 0) {
                digitSum += (val % 10);
                val /= 10;
            }
        }

        return Math.abs(sums - digitSum);
        
    }
}