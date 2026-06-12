/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {


    // let numberOfIncrementOverTheWholeNumsArray =0;
    // let index = 0;
    let ans = [...nums, ...nums];


    // while(numberOfIncrementOverTheWholeNumsArray < 2 ){

    //     ans.push(nums[index])

    //     index+=1;
    //     if(index === nums.length){
    //         index = 0;
    //         numberOfIncrementOverTheWholeNumsArray+= 1;
    //     }
    // }
    return ans;
};