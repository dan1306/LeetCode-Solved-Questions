bool canAliceWin(int* nums, int numsSize) {

    int i = 0;
    int j = 0;

    for(int k = 0; k < numsSize; k++){
        if(nums[k] > 9){
            j+= nums[k];
        }else{
            i += nums[k];
        }
    }

    if(i ==  j){
        return false;
    }
    return true;
    
}