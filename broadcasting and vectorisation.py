#braodcasting 
import numpy as np
#we will add two arrays of different shapes using broadcasting
arr1=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
arr2=np.array([1,2,3])
arr3=arr1+arr2#arr2 is broadcasted to the shape of arr1
# print("Array 1:\n",arr1)
# print("Array 2:\n",arr2)
# print("Array 3:\n",arr3)

discount=10
arr4=arr2-((arr2)*(discount/100))  #boradcasting treats the array itself as a single entity and performs the operation on each element of the array
print("Array after discount:\n",arr4)

#vectorisation
#vectorisation is the process of performing operations on entire arrays rather than individual elements
#this is faster than using loops to perform operations on individual elements
#we will add two arrays using vectorisation
arr5=np.array([1,2,3,4,5])
arr6=np.array([6,7,8,9,10])
arr7=arr5+arr6 #vectorisation
print("Array 5:\n",arr5)
print("Array 6:\n",arr6)
print("Array 7:\n",arr7)
#we will now multiply each element of an array by 2 using vectorisation
arr8=arr5*2
print("Array 8:\n",arr8)
#we will now square each element of an array using vectorisation
arr9=arr5**2
print("Array 9:\n",arr9)
#we will now find the sine of each element of an array using vectorisation
arr10=np.sin(arr5)
print("Array 10:\n",arr10)
#we will now find the exponential of each element of an array using vectorisation
arr11=np.exp(arr5)
print("Array 11:\n",arr11)
#we will now find the square root of each element of an array using vectorisation
arr12=np.sqrt(arr5)
print("Array 12:\n",arr12)
#we will now find the logarithm of each element of an array using vectorisation
arr13=np.log(arr5)
print("Array 13:\n",arr13)
#we will now find the maximum of two arrays using vectorisation
arr14=np.maximum(arr5,arr6)
print("Array 14:\n",arr14)
#we will now find the minimum of two arrays using vectorisation
arr15=np.minimum(arr5,arr6)
print("Array 15:\n",arr15)