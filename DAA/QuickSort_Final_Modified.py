!pip install ipython-autotime
%load_ext autotime
from random import *
def partitionNormal(arr,low,high):
  i = low
  j = high
  pivot = arr[low]
  while(i<j):
    #i = i + 1
    while(arr[i]<=pivot and i<high):
      i = i + 1
    #j = j - 1
    while(arr[j]>=pivot and j>low):
      j = j - 1

    if(i<j):
      arr[i],arr[j] = arr[j],arr[i]
  arr[j],arr[low] = arr[low],arr[j]

  return j

def quickSortNormal(arr,low,high):
  if(low<high):
    p = partitionNormal(arr,low,high)
    quickSortNormal(arr,low,p)
    quickSortNormal(arr,p+1,high)

def partitionRandom(arr,low,high):
  rand_pivot = randrange(low, high)
  arr[low],arr[rand_pivot] = arr[rand_pivot],arr[low]
  return partitionNormal(arr,low,high)

def quickSortRandom(arr,low,high):
  if(low<high):
    p = partitionRandom(arr,low,high)
    quickSortRandom(arr,low,p)
    quickSortRandom(arr,p+1,high)

%load_ext autotime

arr = [1,5,7,-8,9,0,3,4,2]
#arr = [1,3,4,5,6,7,8,9,10,12,13,44,45,67,68,69,100]
#arr = [0,1,3,5,2,4]
quickSortNormal(arr,0,len(arr)-1)
%load_ext autotime
print(arr)

#arr = [1,3,4,5,6,7,8,9,10,12,13,44,45,67,68,69,100]
#arr = [0,3,4,2,1]
#arr = [1,5,7,-8,9,0,3,4,2]
arr = [0,1,3,5,2,4]
arr = [1,5,7,-8,9,0,3,4,2]
quickSortRandom(arr,0,len(arr)-1)
print(arr)