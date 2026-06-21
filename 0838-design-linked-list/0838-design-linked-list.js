var Node = function(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
};


var MyLinkedList = function() {
    this.head = null;  // Top of the stack
    this.last = null;   // Bottom of the stack
    this.length = 0;
};

/** 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
    
    if(index >= 0 && index < this.length){
        let dummy = this.head;
        for(let i = 0; i < this.length; i++){
            if(i === index){
                return dummy.value;
            }else{
                if(dummy)  {
                    console.log("hi", dummy.value)
                    dummy = dummy.next;
                }
               
            }
        }
    }

    return -1;
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) {
    this.addAtIndex(0, val);
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
    this.addAtIndex(this.length, val);
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {

    if(index >= 0 && index <= this.length){
        if(index === 0){
            let newNode = new Node(val);
            if(this.length === 0){
                this.head = newNode;
                this.last = this.head;
            }else{
                newNode.next = this.head;
                this.head.prev = newNode;
                this.head = newNode;
            }

        } else if(index === this.length){
            let newNode = new Node(val);
            newNode.prev = this.last;
            this.last.next = newNode;
            this.last = newNode;
        } else{
            let dummy = this.head;
            for(let i = 0; i < this.length; i++){
                if((i+1) === index){
                    let newNode = new Node(val);
                    newNode.prev = dummy;
                    newNode.next = dummy.next;
                    dummy.next.prev = newNode;
                    dummy.next = newNode;
                    break;
                }else{
                    dummy = dummy.next;
                }
            }
        }
        this.length += 1;
    }
};

/** 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {

   
    if(index >= 0 && index < this.length){
        if(index === 0){
            this.head = this.head.next;
        } else if(index === this.length - 1){
            this.last = this.last.prev;
            this.last.next = null;
        }else{
            let dummy = this.head;
            
            for(let i = 0; i < this.length; i++){
                if(i === index){
                    let dummiesNext = dummy.next;
                    let dummiesPrev = dummy.prev;
                    dummiesNext.prev = dummiesPrev;
                    dummiesPrev.next = dummiesNext;
                    break;
                }else{
                    dummy = dummy.next;
                }
            }
        }
        this.length -= 1;
    }
    
};

/** 
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */