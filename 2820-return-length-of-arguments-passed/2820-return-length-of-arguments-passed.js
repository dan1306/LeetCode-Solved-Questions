/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {

        if(args === []) return 0;
        let i = 1;
        while(1){
            if(args[i - 1] === undefined){
                // i--;
                console.log(args[i-1])
                break;
            }
            i++;
        }
        return i-1;
        // console.log(args)

}

    

/**
 * argumentsLength(1, 2, 3); // 3
 */