'''Given integer n, return all the numbers in the range [1,n]
sorted in lexicographical order
---> you must write an algorithm that runs O(n) time and uses O(1) extra space
input: n=13
output:[1,10,11,12,13,2,3,4,5,6,7,8,9]'''

n=int(input())
l=[]
for i in range (1,n+1):
    l.append(str(i))
    List=sorted(l)
print(list(map(int,List)))

'''
rList=[str(i) for i in range(1,n+1)]
rList.sort()
print(list(map(int,rList)))'''
    
