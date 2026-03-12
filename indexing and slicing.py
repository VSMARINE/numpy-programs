import numpy as np
arr=np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15]])
#we will now access elements of this array using indexing and slicing
#array[start,end,step]
#array[start::end, start::end]
print(arr[0,0])#accessing first element of first row
print(arr[1,2])#accessing 3rd element of 2nd row
print(arr[2,4])#accessing 5th element of 3rd row
print(arr[0,:])#accessing all elements of first row
print(arr[:,1])#accessing all elements of 2nd column
print(arr[1:3,2:4])#accessing elements from 2nd row to 3rd row and 3rd column to 4th column
print(arr[:2,:3])#accessing elements from 1st row to 2nd row and
print(arr[::2,::2])#accessing elements from 1st row to 3rd row and 1st column to 5th column with a step of 2
print(arr[::-1,::-1])#accessing all elements in reverse order
print(arr[1:,2:])#accessing elements from 2nd row to end and 3rd column to end
print(arr[:-1,:-1])#accessing elements from start to 2nd last row and start to 2nd last column
print(arr[::,::])#accessing all elements of the array
print(arr[1,::2])#accessing elements of 2nd row with a step of 2
print(arr[::2,1])#accessing elements of 2nd column with a step of 2
print(arr[::2,::3])#accessing elements of the array with a step of 2 in rows and 3 in columns
print(arr[1:,:3])#accessing elements from 2nd row to end and 1st column to 3rd column
print(arr[:2,3:])#accessing elements from start to 2nd row and 4th column to end
print(arr[1:3,::2])#accessing elements from 2nd row to 3rd row and all columns with a step of 2
print(arr[::2,2:])#accessing elements of all rows with a step of 2 and 2nd column to end
print(arr[::,1:4])#accessing elements of all rows and 2nd column to 4th column 
print(arr[1:3,1:4])#accessing elements from 2nd row to 3rd row and 2nd column to 4th column
print(arr[::3,::2])#accessing elements of all rows with a step of 3 and all columns with a step of 2
print(arr[::2,::3])#accessing elements of all rows with a step of 2 and all columns with a step of 3
print(arr[1:,:])#accessing elements from 2nd row to end and all columns
print(arr[:,:3])#accessing elements of all rows and 1st column to 3rd column
print(arr[::,::2])#accessing elements of all rows and all columns with a step of 2
print(arr[::,::3])#accessing elements of all rows and all columns with a step of 3
print(arr[::2,1:])#accessing elements of all rows with a step of 2 and 2nd column to end
print(arr[1:,::])#accessing elements from 2nd row to end and all columns
print(arr[:2,::])#accessing elements from start to 2nd row and all columns
print(arr[::,1:])#accessing elements of all rows and 2nd column to end
print(arr[::,::-1])#accessing all elements of the array in reverse order
print(arr[::-1,::])#accessing all elements of the array in reverse order
print(arr[::-1,1:4])#accessing elements of all rows in reverse order and 2nd column to 4th column
print(arr[1:3,::-1])#accessing elements from 2nd row to 3rd row and all columns in reverse order
print(arr[::2,::-1])#accessing elements of all rows with a step of 2 and all columns in reverse order
print(arr[::-1,::2])#accessing elements of all rows in reverse order and all columns with a step of 2
print(arr[1:3,::-2])#accessing elements from 2nd row to 3rd row and all columns in reverse order with a step of 2
print(arr[::,::-2])#accessing elements of all rows and all columns in reverse order with a step of 2
print(arr[::-1,1:])#accessing elements of all rows in reverse order and 2nd column to end
print(arr[::2,1:4])#accessing elements of all rows with a step of 2 and 2nd column to 4th column
print(arr[1:3,::3])#accessing elements from 2nd row to 3rd row and all columns with a step of 3
print(arr[::3,::])#accessing elements of all rows with a step of 3 and all columns  
print(arr[::,::3])#accessing elements of all rows and all columns with a step of 3
print(arr[::3,1:])#accessing elements of all rows with a step
print(arr[::3,1:])#accessing elements of all rows with a step of 3 and 2nd column to end
print(arr[1:,::3])#accessing elements from 2nd row to end and all columns with a step of 3
print(arr[:2,::2])#accessing elements from start to 2nd row and all columns with a step of 2
print(arr[::2,:3])#accessing elements of all rows with a step of 2 and 1st column to 3rd column
print(arr[::3,:3])#accessing elements of all rows with a step of 3 and 1st column to 3rd column
print(arr[1:3,:3])#accessing elements from 2nd row to 3rd row and 1st column to 3rd column
print(arr[:,::-3])#accessing elements of all rows and all columns in reverse order with a step of 3
print(arr[::,::-3])#accessing elements of all rows and all columns in reverse order with a step of 3
print(arr[::-1,::3])#accessing elements of all rows in reverse order and all columns with a step of 3