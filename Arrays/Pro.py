# <-------------- 1) Reverse of Array ------------------>

def Reverse(l):
    n=len(l)
    i=0
    j=n-1
    while(i<j):
        temp=l[i]
        l[i]=l[j]
        l[j]=temp
        i+=1
        j-=1
l=[]
n=int(input("enter no of elements"))
for i in range(0,n):
    l.append(int(input()))

Reverse(l)
print("Reverse of an Array is",l)

# ---------------------------------->


#  <-------------------- 2) Find Minimum And Maximum Of An Array --------------->

l=[]
n=int(input("enter no of elements"))
for i in range(0,n):
    l.append(int(input()))

for i in range(len(l)):
    max=l[0]
    min=l[0]
    if(l[i]>max):
        max=l[i]
    if(l[i]<min):
        min=l[i]

print("maximum of An Array is : ",max)
print("Minimum of An Array Is : ",min)

#-------------------------------------------------------------------------------->

# <-------------------- 3) Find the Frequency of paticular given integer--------------->

def findFrequency (arr, x):
    dt=dict()
    for i in range(len(arr)):
        if arr[i] in dt:
            dt[arr[i]]+=1
        else:
            dt[arr[i]]=1
    if x in arr:
        return dt[x]
    else:
        return 0

arr=[1,2,2,2,2,2,2]
x=2
res=findFrequency(arr,x)
print(res)
  
#   output:-6


#<------------------------------- 4)Subarray with given sum -------------------------->
# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4

def  findsubarray(arr,n,s):
    num_sum=0
    index1=0
    index2=0
    while index2<n:
        num_sum+=arr[index2]
        while num_sum>s:
            num_sum-=arr[index1]
            index1+=1
        if num_sum==s:
            return arr[index1+1,index2+1]
        index2+=1
    return -1
arr=[1,2,3,7,5]
N=len(arr)
s=12
res=findsubarray(arr,N,s)

#--------------------------------------------------------------->

#<--------------------------------- 5) Move all negative elements to end -------------------->

arr=[1, -1, 3, 2, -7, -5, 11, 6]
n=len(arr)
l1=[]
l2=[]
for i in range(len(arr)):
    if(arr[i]>=0):
        l1.append(arr[i])
    if(arr[i]<0):
        l2.append(arr[i])
l3=l1+l2           
print(l3)

#-------------------------------------------------------------------------------------------->

