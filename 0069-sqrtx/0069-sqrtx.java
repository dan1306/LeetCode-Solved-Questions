class Solution {
    public int mySqrt(int x) {
        int i = 0;
        int j = x;
        int z = 0;

        while( i <= j){
            System.out.println(i + " " + j);
            int mid = (i+j) / 2;
            long midSqred = (long) mid * mid; ;

            if(midSqred > x){
                j = mid - 1;
            }else{
                if(midSqred == x) return mid;
                if(mid > z) {
                    z = mid;
                }
                i = mid + 1;
            }
            
        }
        return z;
    }
}

