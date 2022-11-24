x=input("enter ch: ")
if ((x>="a" and x<='z') or (x>="A" and x<="Z")):
	print("ye")
else:
	print("nah")
a=input("num1: ")
b=input("num2: ")
print("before swap num1: ",a,"\n num2: ",b)
c=a
a=b
b=c
print("\n\nafter swap num1: ",a," \nnum2: ",b)
l1=[1,2,3,4,5,6,7,8,9]
l2=[1,2,3,4,5,6,7,8,9]
l3=[]
for i in range(0,9):
	l3.append(l1[i]+l2[i])
print(l3)