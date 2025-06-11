f=open("c:\\users\\MICLAB\\Desktop\\demo.txt",'r')
data=f.read()
lw=data.spilt()
d={}
for word in lw:
    if word not in d:
        d[word]=1
    else:
        d[word]=d[word]+1
    print(d)
