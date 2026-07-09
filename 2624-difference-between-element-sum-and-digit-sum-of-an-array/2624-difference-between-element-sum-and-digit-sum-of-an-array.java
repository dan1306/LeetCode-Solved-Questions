class Solution {
    public int differenceOfSum(int[] nums) {

        int sums = 0;
        int digitSum = 0;

        for(int i = 0; i < nums.length; i++){
            sums+= nums[i];
            if( nums[i] < 10){
                digitSum+= nums[i];
            }else{
                // digitSum+=nums
                // String str = nums[i] + "";
                int temp = nums[i];
                while (temp > 0) {
                    digitSum += temp % 10; // Grabs the last digit
                    temp /= 10;            // Chops off the last digit
                }
            }
        }
        int ans = sums - digitSum;
        if(ans < 0) return(ans * -1);
        return ans;
        // return Math.abs(sums - digitSum);
        
    }
}