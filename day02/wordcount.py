a="the quick brown fox the lazy dog the end"
b={}

for  i in a.split():
    if i in b:
        b[i]=b[i]+1
    else :
        b[i] = 1

print (b)