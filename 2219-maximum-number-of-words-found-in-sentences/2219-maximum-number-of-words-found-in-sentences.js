/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    
//     let a = sentences[0].split(" ")
    
//     console.log(a)
    
    let one = 0
    
    for(let i = 0; i < sentences.length; i++){
        
         let a = sentences[i].split(" ") 
         
         if(a.length > one){
             one = a.length
         }
        
    }
    
    return one
    
};