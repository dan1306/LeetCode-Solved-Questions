/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(str) {
    
    let openbrac = ['(', '[', '{']
  let closebrac = [')', ']', '}']

  let matchbrac = {
    ')': '(',
    '}': '{',
    ']': '['
  }

  let arr = []

  // let braces = {
  //   '(': 0,
  //   ')':0,
  //   '{':0,
  //   '}':0,
  //   '[':0,
  //   ']':0
  // }

  for(let i = 0; i < str.length; i++){

    if(arr.length == 0 && closebrac.includes(str[i])){
        console.log(arr)
      return false
    } else{
      if(openbrac.includes(str[i])){
        arr.push(str[i])
      }else{
        if(closebrac.includes(str[i]) && arr[arr.length -1] == matchbrac[str[i]]){
          arr.pop()
        } else{
            console.log(arr)
          return false
        }
      }
    }
    
  }

  if(arr.length > 0){
      console.log(arr)
    return false
  }
  console.log(arr)
  return true
    
};