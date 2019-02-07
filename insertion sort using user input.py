def inserctionSort(alist):
	for i in range(1,len(alist)):
		p=alist[i]
		j = i
		while j>0 and alist[j-1]>p:
			alist[j]=alist[j-1]
			j=j-1
		alist[j]=p

alist=[]
x=int(input("Write length:"))
for i in range(0,x):
    n=int(input("Enter element"));
    alist.append(n)

print ("before sorting",alist)
inserctionSort(alist)
print ("after sorting",alist)
