class Solution {
    public int[] numberGame(int[] nums) {
        if(nums.length == 0) return nums;
        int i = 0;
        int j = nums.length - 1;
        int index = 0;
        // System.out.print(i);
        int[] returnArr = new int[nums.length];
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

            // // j--;
            // if(i + 2 > j){
            //     int placeholdera = nums[alice];
            //     int placeholderb = nums[bob];
            //     nums[i] = placeholderb;
            //     nums[i+1] = placeholdera;
            // } else {
            // System.out.print(i + " " + (i+1) + "\n");
            //  System.out.print(alice+ " " + bob+ "\n");
            // System.out.print(nums[alice] + " " + nums[bob]+ "\n");
            // int placeHolder1 = nums[i];
            // nums[i] = nums[bob];
            // nums[bob] = placeHolder1;

            // int placeHolder2 = nums[i + 1];
            // nums[i + 1] = nums[alice];
            // nums[alice] = placeHolder2;
            // System.out.print(nums[i] + " " + nums[i+1] + "\n\n"); 
            // }


            i += 2; 
        }

        return nums;
        
    }

    
}