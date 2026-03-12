'''
we wil learn some advanced numpy functions
'''
import numpy as np
arr=np.array([[1,2,3,4,5,6]])
#we can insert at any axis at any position in the array usign insert() function
#syntax: np.insert(array, position, values, axis)

#this does not modify the original array rather it returns a new array with the values inserted at the specified position along the specified axis

'''
array: input array
position: index at which values are to be inserted
values: values to be inserted
axis: axis along which to insert values. If axis is 0 then values are inserted as rows. If axis is 1 then values are inserted as columns. If axis is None then array is flattened before insertion.
'''
new_arr=np.insert(arr,1,32,axis=1)#inserting 32 at index 1 along axis 1(columns)
print(new_arr)

arr2=np.array([[1,2,3],
               [4,5,6]])
new_arr2=np.insert(arr2,2,[10,11,12],axis=0)#inserting [10,11,12] at index 2 along axis 0(rows)
print(new_arr2)


#we will append values using append() function
'''
append() funtion appends values at the end of the array along the specified axis so we do not need to specify the position
syntax: np.append(array, values, axis)
array: input array
values: values to be appended
axis: axis along which to append values. If axis is 0 then values are appended as rows. If axis is 1 then values are appended as columns. If axis is None then array
'''
new_arr3=np.append(arr2,[[7],[8]],axis=1)#appending [7,8,9] at the end along axis 1(columns)
print(new_arr3)
new_arr4=np.append(arr2,[[7,8,9]],axis=0)#appending [7,8,9] at the end along axis 0(rows)
print(new_arr4)

'''
now we will add two array using numpy's concatenate() function
syntax: np.concatenate((array1, array2, ...), axis)
array1, array2, ...: input arrays to be concatenated. They must have the same shape along all axes except the one specified by axis.
axis: axis along which to concatenate the arrays. If axis is 0 then arrays are concatenated along rows. If axis is 1 then arrays are concatenated along columns. Default is 0.
'''
arr5=np.array([[11,12,13,14,15,16]])
arr6=np.array([[11,12,13]])
new_arr5=np.concatenate((arr,arr5),axis=0)#concatenating arr and arr5 along axis 0(rows)
print(new_arr5)
print(np.concatenate((arr,arr5),axis=1))#concatenating arr and arr5 along axis 1(columns)
print(np.concatenate((arr6,arr2),axis=0))#concatenating arr6 and arr2 along axis 0(rows)

'''
we can delete any element or row or column using delete() funtion
note: this cannot delete a specific element in a 2D array it can only delete a specific row or column
note: this does not modify the original array rather it returns a new array with the values deleted at the specified position along the specified axis
syntax: np.delete(array, position, axis)
'''

print(np.delete(arr2,1,axis=0))
print(arr2)#original array is not modified
print(np.delete(arr,4,axis=1))
print(arr)#original array is not modified


'''
we can split an array into multiple sub-arrays using split() function
i we want to split an array in to vertical sub-arrays we use vsplit() funtion and for horizontal sub-arrays we use hsplit() function
syntax: np.split(array, number_of_splits, axis)
array: input array to be split
number_of_splits: number of splits to be made. It must be an integer and must evenly divide the axis length.
axis: axis along which to split the array. If axis is 0 then array is split along rows. If axis is 1 then array is split along columns. Default is 0.

'''


arr7=np.array([[1,2,3,4,5,6,7,8],
               [9,10,11,12,13,14,15,16],
               [17,18,19,20,21,22,23,24],
               [25,26,27,28,29,30,31,32]])
new_arr6=np.split(arr7,2,axis=1)#splitting arr7 into 2 sub-arrays along axis 1(columns)
print(new_arr6)
new_arr7=np.split(arr7,2,axis=0)#splitting arr7 into 2 sub-arrays along axis 0(rows)
print(new_arr7)

new_arr8=np.vsplit(arr7,2)#splitting arr7 into 2 sub-arrays along vertical axis
print(new_arr8)
new_arr9=np.hsplit(arr7,4)#splitting arr7 into 4 sub-arrays along horizontal axis
print(new_arr9)

