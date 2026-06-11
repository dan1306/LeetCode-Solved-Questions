/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {

    let maxConsecutiveOnes = 0;
    let incremnentMe = 0;
    for(let i = 0; i < nums.length; i++){
        if(nums[i] === 1){
            incremnentMe += 1;
        } else{
            if(incremnentMe > maxConsecutiveOnes) {
                maxConsecutiveOnes = incremnentMe;
            }
            incremnentMe = 0
        }
    }
          if(incremnentMe > maxConsecutiveOnes) {
                maxConsecutiveOnes = incremnentMe;
            }
    return maxConsecutiveOnes;
    
};