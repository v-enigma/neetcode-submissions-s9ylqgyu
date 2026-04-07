class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda item: item[0] )
        def isOverlaped(A:List[int], B:List[int]):
            if A[0] <= B[0] :
                if B[0] <= A[1]:
                    if A[1] <= B[1]:
                        return [A[0], B[1]]
                    else:
                        return [A[0] ,A[1]]
                else:
                    return "NoOverlap"
            else:
                if A[0] <= B[1]:
                    if B[1] <= A[1]:
                        return [B[0],A[1]]
                    else:
                        return [B[0], B[1]]
                else:
                    return "NoOverlap"
        isMerged = True
        while(len(intervals)>=2 and isMerged):
            result = []
            i = 0
            #remaining = len(intervals)
            while(i<len(intervals)):
                print(intervals)
                remaining = len(intervals) - i-1
                if remaining == 0:
                    result.append(intervals[i])
                    i = i + 1
                else:
                    overlap = isOverlaped(intervals[i], intervals[i+1])
                    if overlap != "NoOverlap":
                        result.append(overlap)
                        i=i+2
                    else:
                        result.append(intervals[i])
                        
                        i = i + 1
                
            if len(result) == len(intervals):
                isMerged = False
            intervals = result 
        return intervals
        
            

        

        
        

                    

                


        