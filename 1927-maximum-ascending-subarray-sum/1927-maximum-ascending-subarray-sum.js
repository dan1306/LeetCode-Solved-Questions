/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAscendingSum = function(nums) {
    let highest = 0;
    let dummy = 0;
    for(let i = 0; i < nums.length; i++){
        if(i == 0){

            dummy = nums[i];
            highest = dummy;
        } else if(i > 0){
            // if(dummy == 0){
            //     console.log(i)
            //     dummy = nums[i]
            //     if(dummy > highest){
            //             highest = dummy;
            //     }
            // } else {
                if(nums[i] > nums[i -1]){
                    dummy+= nums[i];
                    // console.log(i)
                    if(dummy > highest){
                        highest = dummy;
                    }
                }else {
                    // console.log(dummy);
                    dummy = nums[i];
                }
            // }
        }
    }
    console.log(highest)
    return highest;
    
};