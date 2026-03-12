#we will maniputale the shape of the arrays using reshape, flatten, ravel, transpose, swapaxes, and resize functions
import numpy as np
arr=np.array([[1,2,3,4,5,6],
              [7,8,9,10,11,12],
              [13,14,15,16,17,18]])
#we will now reshape this array to 2 rows and 9 columns
reshaped_arr=arr.reshape(2,9)
print("Reshaped array:\n",reshaped_arr)

#ravel-->returns a flattened array as a view of the original array
#flatten-->returns a copy of the original array flattened


#we will now flatten this array to 1D array
flattened_arr=arr.flatten() #it return a copy of the original array
print("Flattened array:\n",flattened_arr)
#we will now ravel this array to 1D array
raveled_arr=arr.ravel()#it return a flattened array as a view of the original array
print("Raveled array:\n",raveled_arr)
#we will now transpose this array
transposed_arr=arr.transpose()
print("Transposed array:\n",transposed_arr)