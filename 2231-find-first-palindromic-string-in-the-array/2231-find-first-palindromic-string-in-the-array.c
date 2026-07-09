#include <stdio.h>
#include <string.h>

char* firstPalindrome(char** words, int wordsSize) {
    int l = -1;
    for(int k = 0; k < wordsSize; k++){
        char* firstWord = words[k];
        int i = 0;
        int j = strlen(firstWord) - 1;
        while (i <= j){
            printf("i is %c, j is %c %d\n", firstWord[i], firstWord[j], k);
            if(firstWord[i] != firstWord[j]) {
                l = -1;
                break;
            }
            i+=1;
            j-=1;
            l = 1;
        }

        if(l > -1)return words[k];
    }
    // int *ptr = nullptr;
    return "";
    
}