/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */




const countStudents = function(students, sandwiches) {

    class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    pop(){
        if(this.length === 1){
            this.first = null;
            this.last = this.firs; 
            this.length -=1;
        }else if(this.length > 1){
            this.first = this.first.next;
            this.length -=1;
        }

        
    }

    // Add to the back
    append(value) {
        const newNode = new Node(value);
        if (this.length === 0) {
            this.first = newNode;
            this.last = newNode;
        } else {
            this.last.next = newNode;
            this.last = newNode;
        }
        this.length++;
        return this;
    }

    // Take from the front and move to the back
    rotate() {
        // If the list is empty or only has 1 item, nothing changes
        if (this.length <= 1) return this;

        // 1. Hold onto the current first node
        const oldFirst = this.first;

        // 2. Move the 'first' pointer to the second node
        this.first = oldFirst.next;

        // 3. Sever the old first's link to the rest of the list
        oldFirst.next = null;

        // 4. Attach the old first after the current 'last' node
        this.last.next = oldFirst;

        // 5. Update the 'last' pointer to be this node
        this.last = oldFirst;

        return this;
    }

    // Helper to print the list
    toArray() {
        const result = [];
        let current = this.first;
        while (current) {
            result.push(current.value);
            current = current.next;
        }
        return result;
    }
}

    const studentQueue = new LinkedList();
    const sandwhichQueue = new LinkedList();

    for(let i = 0; i < students.length; i++) studentQueue.append(students[i]);
    for(let j = 0; j < sandwiches.length; j++) sandwhichQueue.append(sandwiches[j]);

    let someoneWantsIt = 0;

    while(someoneWantsIt !== studentQueue.length){
        if(studentQueue.first.value === sandwhichQueue.first.value){
            studentQueue.pop();
            sandwhichQueue.pop();
            someoneWantsIt = 0;
        }else {
            studentQueue.rotate();
            someoneWantsIt+= 1;
        }
    }

    
    return studentQueue.length;
    
    
};
