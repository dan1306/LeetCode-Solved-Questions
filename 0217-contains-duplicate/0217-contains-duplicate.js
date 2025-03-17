/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {

    nums.sort();

    let index = 0;

    let inexPlusOne = index + 1;

    while(index < nums.length && inexPlusOne < nums.length){
        if(nums[index] == nums[inexPlusOne]) return true;
        index++;
        inexPlusOne++;
    }

    return false;
    
};