int xorOperation(int n, int start) {

    int nums[n];
    int  returnMe = 0;

    for(int i = 0; i < n; i++) {
        nums[i] = start + 2 * i;
        returnMe = returnMe ^ nums[i];
    }
    return returnMe;


    
}