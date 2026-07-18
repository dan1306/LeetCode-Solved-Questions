/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int findSmallestValueinBST(struct TreeNode* root);

struct TreeNode* deleteNode(struct TreeNode* root, int key) {


    if(!root) return root;
    if(root->val == key ){

        if(!(root->right) && !(root->left)){
            root = NULL;
            return root;
        }else if(!(root->right) && root->left){
            root = root->left;
            return root;
        } else if (!(root->left) && root->right){
            root = root->right;
            return root;
        }else{  
            int s = findSmallestValueinBST(root->right);
            root->right = deleteNode(root->right, s);
            root->val = s;
            return root;
        }

    } else {

        struct TreeNode* copy = root;
        struct TreeNode* pre = NULL;
        while(copy && copy->val != key){
            pre = copy;
            if(key > copy->val ){
                copy = copy->right;
            }else {
                copy = copy->left;
            }
        }


        if(!copy) return root;

        if(!(copy->left) && !(copy->right)){
            if(pre->left && pre->left->val == key) {
                pre->left = NULL;
            } else{
                pre->right = NULL;
            }
        }else if(!(copy->left) && copy->right){
            if(pre->left && pre->left->val == key) {
                pre->left = copy->right;
            } else{
                pre->right = copy->right;
            }
        }else if(!(copy->right) && copy->left){
            if(pre->left && pre->left->val == key) {
                pre->left = copy->left;
            } else{
                pre->right = copy->left;
            }
        }else{
            int smallestVal = findSmallestValueinBST(copy->right);
            copy->right = deleteNode(copy->right, smallestVal);
            copy->val = smallestVal;
        }

        return root;
    }

    
}

int findSmallestValueinBST(struct TreeNode* root){
    // int val = NULL;

    while(root->left){
        root = root->left;
    }

    return root->val;
}