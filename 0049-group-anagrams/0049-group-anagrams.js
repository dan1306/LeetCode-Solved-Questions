/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {


    let a = {};
    let b = [];

    for( let i = 0; i < strs.length; i++){
        let c = strs[i].split('').sort().join('');

        if(c in a){
            b[a[c]].push(strs[i]);

        } else{

            a[c] = b.length;
            b.push([strs[i]]);
        }
    }
    return b;
    
};