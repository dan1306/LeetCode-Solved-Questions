/**
 * @param {number[]} nums
 * @return {number[]}
 */

function sortArray(nums){

  if(nums.length == 1){
    return nums
  }

  let mid = nums.length / 2
  let subLeft = sortArray(nums.slice(0, mid))
  let subRight = sortArray(nums.slice(mid))


  return merge(subLeft, subRight)
}

function merge(subLeft, subRight){

  let res = []
  let r = 0
  let l = 0

  while( l < subLeft.length && r < subRight.length){
    if(subLeft[l] < subRight[r]){
      res.push(subLeft[l])
      l++
    } else{
       res.push(subRight[r])
      r++
    }
  }

  return(res.concat(subLeft.slice(l)).concat(subRight.slice(r)))
}