class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        n=len(messages);l=[];d={}
        if(n==len(senders) and 1<=n and n<=10000):
            for i in range(n):
                if(1<=len(messages[i]) and len(messages[i]) <=100 and 1<=len(senders[i]) and  len(senders[i]) <=100):
                    try:
                        d[senders[i]]=d[senders[i]]+len(messages[i].split())
                    except:
                        d[senders[i]]=len(messages[i].split())
            p=list(d.values())
            p.sort()
            for j in d.keys():
                   if(d[j]==p[-1]):
                        l.append(j)
            l.sort()
            return l[-1]
                        
                   
