from random import *
def partitionNormal(arr,low,high):
  i = low
  j = high
  pivot = arr[low]
  while(i<j):
    i = i + 1
    while(arr[i]>=pivot and i<high):
      i = i + 1
    j = j - 1
    while(arr[j]<pivot and j>low):
      j = j - 1
 
    if(i<j):
      arr[i],arr[j] = arr[i],arr[j]
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
