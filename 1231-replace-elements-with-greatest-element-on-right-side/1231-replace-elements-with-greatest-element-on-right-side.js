/**
 * @param {number[]} arr
 * @return {number[]}
 */

var replaceElements = function(arr) {

    if(arr.length === 0) return arr;
    if(arr.length === 1){
        arr[0] = -1;
        return arr;
    }

    let dummy = []
    let obj = {}
    let ittBack = arr.length - 2;
    while(ittBack >= 0){

        if(ittBack === arr.length -2){
            obj[ittBack] = arr[ittBack + 1]
        }else{
            if(arr[ittBack + 1] > obj[ittBack + 1]){
                obj[ittBack] = arr[ittBack + 1];
            } else{
                obj[ittBack] = obj[ittBack + 1];
            }
        }
        ittBack -= 1;
    }

    for(let i = 0; i < arr.length -1; i++){
        dummy.push(obj[i]);
    }

    dummy.push(-1);
    return dummy;
}


// var replaceElements = function(arr) {

//     if(arr.length === 0) return arr;
//     if(arr.length === 1){
//         arr[0] = -1;
//         return arr;
//     }

//     let dummy = []
//     let maxElemement = null;
//     let indexOfMaElement = null;
//     let whereWeareAtinArr = 0;
//     while(dummy.length < arr.length - 1 ){

//         if((maxElemement && indexOfMaElement) && indexOfMaElement > whereWeareAtinArr){
//             dummy.push(maxElemement)
//         } else{
//             maxElemement = null;
//             indexOfMaElement = null;
//             for(let i = whereWeareAtinArr + 1; i < arr.length; i++){
//                 if(arr[i] > maxElemement || !maxElemement){
//                     indexOfMaElement = i;
//                     maxElemement = arr[i];
//                 }
//             }
//             dummy.push(maxElemement);
//         }
//         whereWeareAtinArr+=1;

//     }
//     dummy.push(-1)
//     return dummy;

// }

// var replaceElements = function(arr) {

//     if(arr.length === 0) return arr;
//     if(arr.length === 1){
//         arr[0] = -1;
//         return arr;
//     }

//     let dummy = [];

//     for(let i = 1; i < arr.length; i++){
//         if(dummy.length === 0 && i === 1){
//             let obj = {
//                 val: arr[i],
//                 // index: i,
//                 numberOfIndexesToOccupy: 1
//             }
//             dummy.push(obj);
//         } else {
//             if(arr[i] === dummy[dummy.length -1].val){
//                 dummy[dummy.length -1].numberOfIndexesToOccupy+=1;
//             } else if(arr[i] > dummy[dummy.length -1].val){
//                 console.log(arr[i], dummy[dummy.length -1].val)
//                 let obj = {
//                     val: arr[i],
//                     // index: i,
//                     numberOfIndexesToOccupy: 1
//                 }    
//                 while(true){
//                     if(dummy.length > 0 && arr[i] > dummy[dummy.length -1].val){
//                         let placeHolder = dummy.pop();
//                         obj.numberOfIndexesToOccupy += placeHolder.numberOfIndexesToOccupy;
//                         continue;
//                     }else if (dummy.length === 0 || dummy[dummy.length -1].val > arr[i]){
//                         dummy.push(obj);
//                         break;
//                     }
//                 }

//             } else if(arr[i] < dummy[dummy.length -1].val){
//                 let obj = {
//                     val: arr[i],
//                     // index: i,
//                     numberOfIndexesToOccupy: 1
//                 }
//                 dummy.push(obj);              
//             }
//         }
//     }

//     let returnMe = [];
//     let startHere = 0;
//     while(startHere !== dummy.length){
//         if(dummy[startHere].numberOfIndexesToOccupy > 0){
//             returnMe.push(dummy[startHere].val);
//             dummy[startHere].numberOfIndexesToOccupy -= 1;
//             continue;
//         } else{
//             startHere+=1 
//         }
//     }
//     returnMe.push(-1);
//     return returnMe;
// };