/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    
    if(n == 1) return 1;
    if (n == 2 ) return 2;

    let one = 1;
    two = 1;
    
    n -= 2;
    let sum;
    for(let i = 0; i <= n; i++){
        sum = one + two;
        one = two;
        two = sum;
    }

    return sum;

};