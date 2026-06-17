/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {

    let corresponding_open = {
        ')': '(',
        '}': '{',
        ']': '['
    };

    let open = "({["
    let openSet = new Set(open);

    let keepTrack = [];

    for(let i = 0; i < s.length; i++){
        if(openSet.has(s[i])){
            keepTrack.push(s[i]);
        } else{
            if(keepTrack.length > 0 && corresponding_open[s[i]] ==  keepTrack[keepTrack.length - 1]){
                keepTrack.pop()
            } else {
                return false;
            }
        }
    }

    if(keepTrack.length > 0) return false;
    return true;
    
};