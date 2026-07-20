int gcd(int a, int b);

int gcdOfOddEvenSums(int n) {
        int i  = 1;
        int odd = 1;
        int even = 2;
        int sumOfEeven = 0;
        int sumOfOdd = 0;

        while(i <= n){
            sumOfEeven += even;
            sumOfOdd += odd;
            odd+=2;
            even+=2;
            i+=1;
            printf("oddSum = %d, evenSum = %d\n", sumOfEeven, sumOfOdd);

        }
        return gcd(sumOfEeven, sumOfOdd);
}

int gcd(int a, int b)
{
    int minOfTwo = ((a < b) ? a : b);
    while(minOfTwo > 0){

        if(a % minOfTwo == 0 && b % minOfTwo == 0){
            break;
        }
        minOfTwo-=1;
    }
    return minOfTwo;
}