file1=open("Doc1.txt","r")
text1=file1.readlines()
#print(text1)

file2=open("Doc2.txt","r")
text2=file2.readlines()
#print(text2)
l=[]
m=""
n=""
for i in text1:
    m+=i
for j in text2:
    n+=j
c=0
m=m.strip()
n=n.strip()
m=m.split("\n") and m.split(".")
n=n.split("\n") and n.split(".")
if '' in m and n:
    m.remove('')
    n.remove('')
for i in m:
    for j in n:
        if i==j:
            l.append(i)
            c+=1
k=""
for i in l:
    k+=i

print(k)
print(c)