# import numpy as np
# #here we will create arrays using default values with help of numpy built in functions
# #command name: zero((k,i,j))--->(for 3D) fills all the elements with zeros
# #zero((i,j))--->(for 2D) fills all the elements with zeros
# #zero(i)--->(for 1D) fills all the elements with zeros
# arr=np.zeros(3)#creates a 1D array with all the elements filled with zeros
# arr2=np.zeros((3,2))#creates a 2D array with all the elements filled with zero
# arr3=np.zeros((4,2,3))#yup that's 3D
# print(arr)
# print(arr2)
# print(arr3)

# #command name:ones((size,size,size))--->fills all the elements with 1s and works same as zeors command
# #rules are same as zeors command
# arr4=np.ones(1)
# arr5=np.ones((3,4))
# arr6=np.ones((2,3,2))
# print(arr6)

# command name:full((k,i,j),value)-->fills all the elements with the value provided by user
# arr7=np.full((3,4),7)#creates a 2D array with all the elements filled with 7
# print(arr7)
# arr8=np.full((2,3,2),9)#creates a 3D array with all the elements filled with 9
# print(arr8)

# command name:arrange(start,end,step)-->creates an array with values in a given range with a specific step
# arr9=np.arange(1,10,1)#creates a 1D array with values from 1 to 9 with a step of 1
# print(arr9)
# arr10=np.arange(1,20,2)#creates a 1D array with values from 1 to 19 with a step of 2
# print(arr10)

# command name:eye(size)-->creates an identity matrix of given size
# arr11=np.eye(3)#creates a 3x3 identity matrix
# print(arr11)

# #.ndim-->gives the dimension of the array
# print(arr11.ndim)
# print(arr5.ndim)
# print(arr3.ndim)

# #.shape-->gives the shape of the array
# print(arr11.shape)
# print(arr5.shape)
# print(arr3.shape)

# #.size-->gives the total number of elements in the array
# print(arr11.size)
# print(arr5.size)
# print(arr3.size)

# #.dtype-->gives the data type of the array
# print(arr11.dtype)
# print(arr5.dtype)
# print(arr3.dtype)

# .astype()-->used to change the data type of the array
# arr13=np.array([1.6,2.5,3.7])
# arr12=arr13.astype(str)
# print(arr13.dtype)
# print(arr12)
# print(arr12.dtype)