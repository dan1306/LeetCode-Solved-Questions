/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    
    return binarySearch(merge(flattened(matrix)), target)
    
    // let arr = merge(flattened(matrix))
    // console.log(arr)
    
};

const binarySearch = (nums, target) => {

  let beg = 0
  let end = nums.length - 1

  let mid = Math.floor((beg + end) / 2)

  while(beg < end){

    if(nums[mid] == target){
      return true
    } else if( nums[mid] > target){
      end = mid - 1
    } else{
       beg = mid + 1
    }
      
    mid = Math.floor(((beg + end) / 2))

  }

  if(nums[mid] == target){
    return true
  }

  return false
  
}

const merge = (arr) =>{
  if(arr.length == 1){
    return arr
  }

  let mid = arr.length / 2
  let subLeft = merge(arr.slice(0, mid))
  let subRight = merge(arr.slice(mid))

  return mergeArr(subLeft, subRight)
}

const mergeArr = (subLeft, subRight) => {

  let res = []
  let l = 0
  let r = 0

  while(l < subLeft.length && r < subRight.length){

    if(subLeft[l] < subRight[r]){
      res.push(subLeft[l])
      l++
    } else {
      res.push(subRight[r])
      r++
    }
    
  }

  return  res.concat(subLeft.slice(l)).concat(subRight.slice(r))
}

const flattened = (arr, lis=[]) => {



    for(let i = 0; i < arr.length; i++){

      if(Array.isArray(arr[i])){
        flattened(arr[i], lis)
      }
      else{
        lis.push(arr[i])
      }

    }

    return lis

}
  