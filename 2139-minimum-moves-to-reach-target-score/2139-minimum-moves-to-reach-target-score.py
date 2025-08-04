class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        s=0
        if(maxDoubles!=0):
            while(target>1 and maxDoubles !=0):
                if(target%2!=0):
                    s=s+1
                target=target//2
                if(target==1):
                    return s+1
                s=s+1
                maxDoubles=maxDoubles-1
        s=s+target-1
        return s
            
            
                
                
        