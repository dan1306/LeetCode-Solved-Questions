#include <iostream>
#include <cstring> // C++ wrapper for C's <string.h>

class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = needle.length();
        int h = haystack.length();

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
};