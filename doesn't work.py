map=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','F','G','H','I','J','K','L','M']
class intme:
    def __init__(self,intin):
        self.value=intin
    def t23(self):
        return map[self.value%23]
    def t529(self):
        return map[(self.value//23)%23]+map[self.value%23]
    def Z3t(self):
        return map.index(self.value)
letter="1"
letters=['A','B','C','D']
import random

while True:
    ans=1
    while True:
        xaxis=input("A.add\tB.sub\tC.mult\tD.div\t")
        if xaxis=='q': break
        for i in range(0,len(letters)): 
            if letters[i] in xaxis: break
        if letters[i] in xaxis: break
    if xaxis=='q': break
    xmin=int(input("y min"))
    if xmin=='q': break
    xmax=int(input("y max"))
    if xmax=='q': break
    ymin=int(input("z min"))
    if ymin=='q': break
    ymax=int(input("z max"))
    if ymax=='q': break
    if xmin>xmax:
        ans=xmin
        xmin=xmax
        xmax=ans
    if ymin>ymax:
        ans=ymin
        ymin=ymax
        ymax=ans
    while ans!='q':
        a=intme(random.randint(xmin,xmax))
        b=intme(random.randint(ymin,ymax))
        while letter not in xaxis:
            letter = letters[random.randint(1,len(letters))-1]
        if letter =='A':
            c=intme(a.value+b.value)
            print(a.t23(),b.t23(),'+')
            ans=input()
            print(c.t529())
        if letter =='B':
            print(a.t23(),b.t23(),'-')
            ans=input()
            c=intme(a.value-b.value)
            print(c.t529())
        if letter =='C':
            print(a.t23(),b.t23(),'*')
            ans=input()
            c=intme(a.value*b.value)
            print(c.t529())
        if letter =='D':
            print(a.t23(),b.t23(),'÷')
            ans=input()
            if b.value==0: break
            c=intme(0)
            bc=intme(0)
            while bc.value%23!=a.value:
                c.value+=1
                bc=intme(b.value*c.value)
            print(c.t23(),bc.t529())

        
        
        
        






















