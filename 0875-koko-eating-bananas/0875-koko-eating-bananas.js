/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    
    let sortedPile = merge(piles)
  
    let remain = sortedPile.length - 1
    
    let k= sortedPile[sortedPile.length - 1]
    
    let beg = 1
    
    let end = sortedPile[sortedPile.length - 1]
    
    let mid = Math.floor((beg + end) / 2)
    
    let lasDig = sortedPile[sortedPile.length - 1]



    while(beg <= end){
        
        


        // console.log(mid)
        ans = h - (maxTime(sortedPile, mid))
                  console.log(ans, mid, (maxTime(sortedPile, mid)))

        // console.log(h, divi, remain, ans)

        if( ans >= 0 ){
          if(mid < k){
            k = mid
            // console.log(k)

          }
          end = mid -1
        }

      else{
        beg = mid + 1
      }

      mid = Math.floor((beg + end) / 2)
        
    }

  return(k) 
    
};

const maxTime = (arr, n) =>{

  let sum = 0

  for (const element of arr) {
    if(element < n){
      sum += 1
    } else{
        let divi = Math.floor(element / n)
        if(element % n !== 0){
          divi += 1
        }
      sum += divi
    }
      
  }

  // console.log(sum)
  return sum
  
}

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

