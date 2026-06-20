var Node = function(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
};


var MyStack = function() {
    this.first = null;
    this.last = null;
    this.length = 0;
};

/** 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    newNode = new Node(x);
    newNode.value = x;
    if(this.length === 0){
        this.first = newNode;
        this.last = this.first;
    } else{
        this.first.next = newNode;
        newNode.prev = this.first;
        this.first = this.first.next;
    }
    this.length += 1;
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function() {
    let returnMe = this.first.value;
    if(this.length > 1){
        this.first = this.first.prev
        this.length -=1 ;
    }else if(this.length === 1){
        this.first = null;
        this.first = this.last;
        this.length -= 1;
    }
    return returnMe;
};

/**
 * @return {number}
 */
MyStack.prototype.top = function() {
    return this.first.value;
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    return this.length === 0;
};

/** 
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */