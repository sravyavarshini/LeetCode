class Solution:
    def digitCount(self, num):
        n=len(num);c=0
        if(1<=n and n<=10):
            p=[]
            for j in num:
                p.append(int(j))
            for i in range(n):
                if(p[i]==p.count(i)):
                    c=c+1
            if(c==n):
                return True
            else:
                return False
        
      