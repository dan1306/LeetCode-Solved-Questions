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
System.out.println("sums: " + sums);
            
            // 2. Print the total digit sum calculated for it
            System.out.println("Digit Sum:       " + digitSum);
            
            // A nice separator line between array indices
            System.out.println("-------------------------");
        return Math.abs(sums - digitSum);
        
    }
}