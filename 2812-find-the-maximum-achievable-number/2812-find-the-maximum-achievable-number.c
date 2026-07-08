/**
 * @param {number} num
 * @param {number} t
 * @return {number}
 */
int theMaximumAchievableX(int num, int t) {

    
    int i = 1;

    while(true){
        int j = i - t;
        int k = num + t;
        if( j == k){
            return i;
        }
        i++;
    }
};