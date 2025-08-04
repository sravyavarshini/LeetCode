class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l=[];c=0;d={};s=list(s)
        for i in s:
            if(i.isalpha()):
                l.append(i)
                c=c+1
            else:
                d[c]=i
                c=c+1
        l=l[::-1]
        for i,j in d.items():
            l.insert(i,j)
        s=""
        for i in l:
            s=s+i
        return s