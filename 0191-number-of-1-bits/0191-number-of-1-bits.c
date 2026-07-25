#include <stdio.h>
#include <math.h>

int hammingWeight(int n) {
    int i = 0;
    long long j = 0;

    int k = 31;

    while(k >= 0){
        // printf("%d\n", k);
        long long l = (long long)round(powl(2, k));
        long long m = l + j; 
        // printf("%lld\n", l);
        if(m <= n){
            printf("k:%d     l:%lld\n", k,l);
            // printf("%lld       %lld\n", l, m);
            printf("%d\n", j);
            j =m;
            i++;
            printf("%d\n\n\n", j);
            if(j == n) break;
        }
        k--;
    }
    return i;
}