class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s="";d={};p=65
        for i in key:
            if(i != " " and (i not in s)):
                s=s+i
        for i in s:
            d[i]=str(chr(p)) 
            p=p+1
        for i in range(len(message)):
            try:
                message=message.replace(message[i],d[message[i]])
            except:
                message=message.replace(message[i],message[i])
        return message.lower()
            
            
        