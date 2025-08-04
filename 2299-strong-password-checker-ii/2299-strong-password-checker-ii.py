class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        s="-!@#$%^&*()+";d=0;a=0;sy=0;du=0;a1=0
        if(1<=len(password) and len(password)<=100):
            if(len(password)>=8):
                for i in range(len(password)):
                    if(password[i].isdigit()):
                        d=d+1
                    elif(password[i].isalpha()):
                        if(password[i].islower()):
                            a=a+1
                        else:
                            a1=a1+1
                    elif(password[i] in s):
                        sy=sy+1
                    if(i-1>=0):
                        if(password[i] == password[i-1]):
                            du=du+1
                            
                if(d>0 and a>0 and sy>0 and a1>0 and du==0):
                    return True
                else:
                    return False
                
            else:
                return False
        