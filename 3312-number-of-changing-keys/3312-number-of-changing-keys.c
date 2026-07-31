#include <stdio.h>
#include <ctype.h>

int countKeyChanges(char* s) {
    // s = toupper((unsigned char) s);
    int i = 0;
    int j = 0;
    while(s[i] != '\0'){
        char a = toupper((unsigned char) s[i]);
        char b = toupper((unsigned char) s[i + 1]);
        
        if(a != b && a != '\0' && b!= '\0'){
            printf("%c %c\n", a, b);
            j++;
            i++;
        } else {
            i++;
        }
    }
    return j;
}