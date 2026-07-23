/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* concatWithReverse(int* nums, int numsSize, int* returnSize) {


    int *myArr = malloc(sizeof(int) * (numsSize * 2));
    if(numsSize == 0){
        return myArr;
    }

    int i = 0;
    int j = (numsSize * 2) - 1;

    while( i <= j){
        // if(i == j){
        //     myArr[i] = nums[i];
        //     break
        // }
        myArr[i] = nums[i];
        myArr[j] = nums[i];
        i++;
        j--;
        
    }

    *returnSize = 2 * numsSize;
    return myArr;
    
}