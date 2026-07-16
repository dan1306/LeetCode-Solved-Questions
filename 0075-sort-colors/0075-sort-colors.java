class Solution {
    public void sortColors(int[] nums) {

        quickSort(0, nums.length - 1, nums);
        
    }


    public static void quickSort(int startPoint, int endPoint, int[] nums){

        if(startPoint >= endPoint) return;
        int i = startPoint - 1;
        int j = startPoint;
        int pivot = endPoint;
        

        while(j < pivot){
            if(nums[j] <= nums[pivot]){
//                int ab = nums[j];
//                int bc = nums[pivot];
//                System.out.println(ab + " " + bc);
                i= i + 1;
                int temp  = nums[i];
                nums[i] = nums[j] ;
                nums[j] = temp;
//                System.out.println(nums[j] + " " + nums[pivot]);
            }
            j= j + 1;
        }
        i+=1;

//        if(i != pivot){
            int temp = nums[i];
            nums[i] = nums[pivot];
            nums[pivot] = temp;
//        }

        quickSort(0, i - 1, nums);
        quickSort(i + 1, j, nums);

    }
 


}