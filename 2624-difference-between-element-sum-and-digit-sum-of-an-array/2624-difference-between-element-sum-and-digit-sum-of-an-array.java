class Solution {
    public int differenceOfSum(int[] nums) {
int sums = 0;
        int digitSum = 0;

        // 1. Enhanced loop cuts index tracking arithmetic
        for (int num : nums) {
            sums += num;
            
            // 2. Clear out the if/else completely to prevent branch mispredictions
            while (num > 0) {
                digitSum += (num % 10);
                num /= 10;
            }
        }
        
        // 3. No condition checks or Math.abs needed; result is always positive
        return sums - digitSum;
    }
}