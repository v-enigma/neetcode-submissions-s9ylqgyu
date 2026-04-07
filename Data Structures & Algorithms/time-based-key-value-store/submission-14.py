class TimeMap:

    def __init__(self):
        self.data_store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data_store:
            self.data_store[key] = []
        self.data_store[key].append((value, timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        items = self.data_store.get(key, -1)
        if items != -1 :
            
            print("INside")
            left = 0 
            right = len(items) -1
            while (left < right):
                print("INside loop")
                middle = (left + right)//2 
                if items[middle][1] == timestamp  :
                    return items[middle][0]
                elif items[middle][1] < timestamp:
                    left = middle+1
                else :
                    right = middle - 1
            if items[left][1] <= timestamp :
                return items[left][0]
            elif left > 0 and items[left - 1][1] <= timestamp:
                return items[left - 1][0]
            else: 
                return ""
        else:
            print("below outside ")
            return ""



        
