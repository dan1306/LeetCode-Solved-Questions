int hammingWeight(int n) {
    
    int i = 0;
    while(n > 0){
        if(n & 1){
            i++;
        }
        n>>=1;
    }
    return i;
}