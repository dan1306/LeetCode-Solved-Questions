class Solution {
    public int subtractProductAndSum(int n) {

        char[] s1 = ("" + n).toCharArray();
        int product = 1; 
        int sum = 0;
        for(int i = 0; i < s1.length; i++){
            int j = Character.getNumericValue(s1[i]);
            product *= j;
            sum += j;
        }

        return product - sum;

        
    }
}