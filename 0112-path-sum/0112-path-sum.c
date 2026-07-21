/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int num;
int *p = &num;

bool traverse(struct TreeNode* root, int t);
bool hasPathSum(struct TreeNode* root, int targetSum) {
    *p = 0;
    return traverse(root, targetSum);
}

bool traverse(struct TreeNode* root, int t){
    if(root == NULL){
        return false;
    }

    *p += root->val;
    if(root->left != NULL){
        bool ret = traverse(root->left, t);
        if(ret) return true;
    }

    if(root->right != NULL){
        bool ret = traverse( root->right, t);
        if(ret) return true;
    }
    if(*p == t && root->right == NULL && root->left == NULL) return true;
    *p-= root->val;
    return false;

}