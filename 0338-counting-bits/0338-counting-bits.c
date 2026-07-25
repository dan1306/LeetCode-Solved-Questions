/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int hammingWeight(int n);

int* countBits(int n, int* returnSize) {
    int* retArr = (int*)malloc(sizeof(int) * (n+1));

    for(int i = 0; i < ( n+1); i++){
        retArr[i] = hammingWeight(i);
    }
    *returnSize = n+1;
    return retArr;
}

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