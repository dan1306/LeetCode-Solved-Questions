int reverseBits(int n) {
    int returnMe = 0;
    int j = 0;
    for(int i = 31; i >= 0; i--){
        int bit = (n & (1U << i)) ? 1 : 0;
        if(bit == 1){
            returnMe |= (1<< j);
        }
        j++;
    }
    return returnMe;
}