func maxProduct(nums []int) int {
    curMax := nums[0]
    curMin := nums[0]
    ans := nums[0]
    for _,x := range nums[1:]{
        if x<0 {
            curMax,curMin=curMin,curMax
        }
        curMax=max(x,x*curMax)
        curMin=min(x,x*curMin)
        ans=max(ans,curMax)
    }
    return ans
}
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}