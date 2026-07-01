#include <stdio.h>
#include <string.h> // Required for strlen in C
int strStr(char* haystack, char* needle) {

    int n = strlen(needle);
    int h = strlen(haystack);
    if(n > h) return -1;
    if(n == 0) return 0;
    

    for(int i = 0; i <= h -n; i++){
        int inNeedle = 0;
        for(int j = i; j < h; j++){
            if(haystack[j] == needle[inNeedle] ){

                inNeedle+=1;

                if (inNeedle == n ){
                    return i;
                }
            } else{
                break;
            }
        }
    }


    return -1;


}