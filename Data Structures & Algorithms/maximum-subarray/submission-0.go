func maxSubArray(nums []int) int {
    curMax := nums[0]
    ans:=nums[0]
    for _,x := range nums[1:]{
       curMax=max(x,x+curMax)
       ans=max(ans,curMax) 
    }
    return ans
}
