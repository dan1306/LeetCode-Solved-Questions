/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {

    if(nums.length === 0) return nums.length;
    if(nums.length === 1){
        if(nums[0] === val) nums.pop();
        return nums.length;
    }
    
    let starting_index = nums.length - 1; 
    
    while(starting_index >= 0 ){
    
        if(nums[starting_index] === val){
            console.log(nums[starting_index], val)
            if(!nums[starting_index + 1] && starting_index === nums.length - 1 && nums[starting_index] === val){
                console.log('ehere')
                nums.pop();
                // starting_index -= 1;
                // continue;
            }else {
                let change_index = starting_index;
                let change_to_index = starting_index + 1;
                while(change_index !== nums.length - 1){
                    nums[change_index]= nums[change_to_index];
                    change_index += 1;
                    change_to_index += 1;
                }
                nums.pop();
                // starting_index -= 1;
                // continue;
            }   
        }

        starting_index -= 1;
    
    }

    return nums.length;
    
};

// console.log(removeElement([0,4,4,0,4,4,4,0,2], 4));
