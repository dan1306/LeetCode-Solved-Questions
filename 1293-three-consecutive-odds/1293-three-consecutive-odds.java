class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {

        int i = 0;

        for(int j = 0; j < arr.length; j++){
            if(arr[j] % 2 == 0) {
                i = 0;
            }
            else{
                i += 1;
            }
            System.out.println(arr[j] + " " + i); 
            if(i == 3) return true;
        }
        return false;
        
    }
}