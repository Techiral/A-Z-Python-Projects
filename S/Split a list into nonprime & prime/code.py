n=int(input("ENTER THE SIZE OF THE list1"))
p=[]
np=[]
l=[]
o=[]
f=0
print("Enter the no.s")
for i in range(0,n):
  e= int(input())
  for j in range(1,n):
    if(e%j==0):
    f+=1
    if(f==1):
      p.append(e)
    else:
      np.append(e)
f=0
print("prime list")
print(p)
print("Non prime list")
print(np)
