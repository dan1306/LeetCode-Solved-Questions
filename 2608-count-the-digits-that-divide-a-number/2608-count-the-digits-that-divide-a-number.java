class Solution {
    public int countDigits(int num) {

        char[] s1 = ("" + num).toCharArray();
        int n = 0;

        for(int i = 0; i < s1.length; i++){
            if((num % (s1[i]-'0')) == 0){ 
                n++;
            }
        }
        return n;
    }
}