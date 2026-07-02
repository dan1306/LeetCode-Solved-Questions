class Solution {
    public int[] numberGame(int[] nums) {
        if(nums.length == 0) return nums;
        int i = 0;
        int j = nums.length - 1;
        while( i <= j){
           
            int alice = -1;
            int bob = -1;

            for(int k = i; k  <= j; k++){
                if(alice == -1){
                    alice = k;
                }else if (nums[k] < nums[alice] ){
                    alice = k;
                }
            }
            // j--;
            for(int l = i; l  <= j; l++){
                if(l == alice) continue;
                if(bob == -1){
                    bob = l;
                }else if (nums[l] < nums[bob] ){
                    bob = l;
                }
            }

            if(bob != i){
                if( i == alice){
                    alice = bob;
                }
                int placeHolder1 = nums[i];
                nums[i] = nums[bob];
                nums[bob] = placeHolder1;

            }

            if(alice != (i + 1 )){
                int placeHolder2 = nums[i + 1];
                nums[i + 1] = nums[alice];
                nums[alice] = placeHolder2;
            }


            i += 2; 
        }

        return nums;
        
    }

    
}