class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def Overlap(items: List[List[int]]):
            merge = [items[0]]
            i = 1
            while( i < len(items)):
                if merge[-1][1] >= items[i][0]:
                    if merge[-1][1] < items[i][1]:
                        merge[-1][1] = items[i][1]
                else:
                    merge.append(items[i])
                i = i+1
            return merge

        i = 0
        last = False
        while(i< len(intervals)):
            if intervals[i][0] > newInterval[0]:
                
                break
            if i == len(intervals)-1:
                    intervals[i][0] < newInterval[0]
                    last = True
            i = i+1
        
        if i == 0 or i < len(intervals) or last:
            print("inside")
            intervals.insert(i,newInterval)
            intervals = Overlap(intervals)
        return intervals   

                

        
        