import re
num=input()
num=int(num)
jj=list()
i=0
while(i!=num):
    inp=input()
    jj.append(inp)
    i+=1
    
sen=''.join(jj)
wordList = re.sub("[^\w]", " ",  sen).split()
pal=[]
for step in wordList:
    y=step[::-1]
    if(step==y):
        pal.append(step)
    else:
        pass
if (len(pal)==0):
    print("No palindrome words found :(")
else:
    print("Palindrome words in the text are: "+", ".join(str(x) for x in pal))
    