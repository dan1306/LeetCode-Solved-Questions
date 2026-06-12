/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
        
        let x = 0;

        let listOfIntToAdd = [];

        for(let i = 0; i < operations.length; i++){
            let attemptToChangeToAnInt = Number(operations[i]);
            if(attemptToChangeToAnInt){
                listOfIntToAdd.push(attemptToChangeToAnInt)
            }else if(operations[i] == "C" ){
                if(listOfIntToAdd.length >= 1){
                    listOfIntToAdd.pop();
                }
            } else if(operations[i] == "D" ){
                if(listOfIntToAdd.length >= 1){
                    listOfIntToAdd.push(listOfIntToAdd[listOfIntToAdd.length - 1] * 2);
                }
            } else if(operations[i] == "+"){
                if(listOfIntToAdd.length >1){
                    listOfIntToAdd.push(listOfIntToAdd[listOfIntToAdd.length -1 ] + listOfIntToAdd[listOfIntToAdd.length - 2]);
                }
            }
        }

        for(let i = 0; i < listOfIntToAdd.length; i++){
            x+= listOfIntToAdd[i];
        }

        return x;
};