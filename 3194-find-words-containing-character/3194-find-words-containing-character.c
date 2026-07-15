/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {

    int* ize = malloc(wordsSize * sizeof(int));
    int z = 0;
    for(int i = 0; i < wordsSize; i++){
        int j = 0;
        char* c = *(words + i);
        while(c[j] != '\0'){
            if(c[j] == x){
                ize[z] = i;
                z+=1;
                break;
            }
            j+= 1;
        }
    }

    if(z != wordsSize){
        ize = realloc(ize, z * sizeof(int));
    }
    *returnSize = z;
    return ize;
    
}