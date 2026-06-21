/**
 * @param {string} homepage
 */

var Node = function(value) {
    this.val = value;
    this.next = null;
    this.pre = null;
};


var BrowserHistory = function(homepage) {
    this.head = new Node(homepage);
    this.tail = this.head;
    this.curr = this.head;
    this.length = 1; 
};

/** 
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function(url) {
    if(this.curr === this.tail){
        this.curr.next = new Node(url);
        this.curr.next.pre = this.curr;
        this.curr =this.curr.next;
        this.tail = this.curr;
    }else{
        this.curr.next = new Node(url);
        this.curr.next.pre = this.curr;
        this.curr = this.curr.next;
        this.tail = this.curr;
    }
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function(steps) {
    
    while(steps !== 0 && this.curr.pre !== null){
        this.curr = this.curr.pre;
        steps -= 1;
    }

    return this.curr.val;
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function(steps) {
    
    while(steps !== 0 && this.curr.next !== null){
        this.curr = this.curr.next;
        steps -= 1;
    }

    return this.curr.val;
};

/** 
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */