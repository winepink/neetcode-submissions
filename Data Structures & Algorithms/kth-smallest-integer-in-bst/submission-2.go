/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func kthSmallest(root *TreeNode, k int) int {
    count := 0
    ans := 0
    var inorder func(*TreeNode)
    inorder=func(node *TreeNode){
        if node ==nil{
            return 
        }
        inorder(node.Left)
        count ++
        if count == k{
            ans = node.Val
            return
        }
        inorder(node.Right)
    }
    inorder(root)
    return ans
}
