/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void  printArr(struct ListNode* head);


struct ListNode* insertionSortList(struct ListNode* head) {

    struct ListNode* curr = head;
    
    int sorted = 0;
    struct ListNode* pre =  NULL;
    while(curr != NULL){

        if(sorted == 0){
            pre = curr;
            curr = curr->next;
            sorted++;
            continue;
        }   
        struct ListNode* dummy = head;
        struct ListNode* prePre =  NULL;
        for(int i = 0; i < sorted; i++){
            if(dummy->val > curr->val){
                if(i == 0){
                    if(sorted == 1){
                        dummy->next = curr->next;
                        curr->next = dummy;
                        head = curr;
                        curr = dummy;
                    }else{
                        pre->next = curr->next;
                        curr->next = dummy;
                        head = curr;
                        curr = pre;
                    }
                   
                }else{
                    pre->next = curr->next;
                    curr->next = prePre->next;
                    prePre->next = curr;
                    curr = pre;
                }
                break;
            }
            prePre = dummy;
            dummy = dummy->next;
        
        }
        sorted++;
        pre = curr;
        curr = curr->next;
    }
    return head;
}




void printArr(struct ListNode* head){
    
    
    
    printf("[");
    while(head != NULL){
        printf("%d", head->val);
        if(head->next != NULL) printf(", ");
        head = head->next;
    }
    printf("]\n");
    
}



                // // printf("The value of x is %d and the value of y is %d\n Before:", curr->val, dummy->val);
                // printArr(head);
                // struct ListNode* first = dummy;
                // struct ListNode* sec = curr;
                // dummy->val = curr->val;
                // curr->val = first;
                // // printf("After:");
                // // printArr(head);