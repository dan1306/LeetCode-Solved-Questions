/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* insertIntoBST(struct TreeNode* root, int val) {

    if(!root){
        struct TreeNode* newNode = malloc(sizeof(struct TreeNode));
        newNode->val = val; 
        newNode->left = NULL;
        newNode->right = NULL;
        root = newNode;
        return root;
    }

    struct TreeNode* copy = root;
    struct TreeNode* pre = NULL;

    while(copy){
        pre = copy;
        if(val <= copy->val){
            copy = copy->left;
        } else {
            copy = copy->right;
        }
    }

    if(val > pre->val) {
        struct TreeNode* newN = malloc(sizeof(struct TreeNode));
        newN->val = val; 
        newN->left = NULL;
        newN->right = NULL;
        pre->right = newN;
    } else {
        struct TreeNode* newN = malloc(sizeof(struct TreeNode));
        newN->val = val; 
        newN->left = NULL;
        newN->right = NULL;
        pre->left = newN;
    }

    return root;
    
}