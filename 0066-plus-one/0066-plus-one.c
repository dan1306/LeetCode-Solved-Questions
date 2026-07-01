/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void flipArray(int* arr, int size);
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int *ptr = (int *)malloc(sizeof(int) * (digitsSize + 1 ));
    
    *returnSize = 0;
    int keepAddingOne = 1;
    int j = 0;
    for(int i = digitsSize - 1; i >= 0; i--){
        if(keepAddingOne == 1){
            int add = digits[i] + 1;
            if (add == 10 && i != 0){
                ptr[j] = 0;
            }else if (add == 10 && i == 0){
                ptr[j] = 0;
                j = j + 1;
                ptr[j] = 1;
            }else{
                ptr[j] = add;
                keepAddingOne = 0;
            }
        }else{
            ptr[j] = digits[i];
        }
        j++;
    }
    // }
    if (j > 0 && j != digitsSize + 1) {
        ptr = (int*)realloc(ptr, sizeof(int) * j);
    }
    *returnSize = j;
    flipArray(ptr, j);
    return ptr;
}

void flipArray(int* arr, int size) {
    int start = 0;
    int end = size - 1;
    
    // Move toward the middle from both sides
    while (start < end) {
        // Swap the elements using a temporary holding variable
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        
        // Move the trackers closer together
        start++;
        end--;
    }
}