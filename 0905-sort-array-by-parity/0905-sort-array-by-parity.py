class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p=[];l=[]
        for i in nums:
                if(i%2==0):
                    l.append(i)
                else:
                    p.append(i)
        for i in p:
            l.append(i)
        return l