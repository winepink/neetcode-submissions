func eraseOverlapIntervals(intervals [][]int) int {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })
    rem:=0
    prev:=intervals[0][1]
    for _,interval := range intervals[1:]{
        st:=interval[0]
        end:=interval[1]
        if st>=prev{
            prev=end
        } else {
            rem++
            prev=min(prev,end)
        }
    }
    return rem
}
