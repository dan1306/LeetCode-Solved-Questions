
var MinStack = function() {
    this.stack = [];
    this.minStack = [];
    this.length = 0;
};

/** 
 * @param {number} value
 * @return {void}
 */
MinStack.prototype.push = function(value) {
    this.stack.push(value);
    if(this.length === 0){
        this.minStack.push(value);
    } else {
        if(this.minStack[this.length - 1] <= value){
            this.minStack.push(this.minStack[this.length - 1]);
        } else {
            this.minStack.push(value);
        }
    }
    this.length+= 1;
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.stack.pop();
    this.minStack.pop();
    this.length -= 1;
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
   return this.stack[this.length -1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
   return this.minStack[this.length -1];
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(value)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */



//  let keepTrackofMinElementInTheStack = []
// var MinStack = function() {
//     return [];
// };

// /** 
//  * @param {number} value
//  * @return {void}
//  */
// MinStack.prototype.push = function(value) {
//     MinStack.push(value)
//     if(keepTrackofMinElementInTheStack == []){
//         keepTrackofMinElementInTheStack.push(value)
//     } else{
//         if(value <= keepTrackofMinElementInTheStack[keepTrackofMinElementInTheStack.length - 1]){
//             keepTrackofMinElementInTheStack.push(keepTrackofMinElementInTheStack[keepTrackofMinElementInTheStack.length - 1])
//         } else{
//             keepTrackofMinElementInTheStack.push(value);
//         }
//     }
// };

// /**
//  * @return {void}
//  */
// MinStack.prototype.pop = function() {
//     MinStack.pop()
//     keepTrackofMinElementInTheStack.pop()
// };

// /**
//  * @return {number}
//  */
// MinStack.prototype.top = function() {
//     return MinStack[MinStack.length - 1]
// };

// /**
//  * @return {number}
//  */
// MinStack.prototype.getMin = function() {
//     keepTrackofMinElementInTheStack[keepTrackofMinElementInTheStack.length -1]
// };

// /** 
//  * Your MinStack object will be instantiated and called as such:
//  * var obj = new MinStack()
//  * obj.push(value)
//  * obj.pop()
//  * var param_3 = obj.top()
//  * var param_4 = obj.getMin()
//  */