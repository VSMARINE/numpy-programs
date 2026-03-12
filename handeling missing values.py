import numpy as np
#handeling missing values in numpy arrays
arr=np.array([1,2,np.nan,4,5,np.nan,7,8,9,10])
#we can use np.isnan() function to find the missing values in the array
missing_values=np.isnan(arr)
print("Missing values:",missing_values)
#we can use np.nan_to_num() function to replace the missing values with a specified value
arr5=np.nan_to_num(arr)#replaces missing values with 0 by default if no value is specified
print("Array after replacing missing values with 0 by default:",arr5)
arr2=np.nan_to_num(arr,nan=0)#replacing missing values with 0
print("Array after replacing missing values with 0:",arr2)
arr3=np.nan_to_num(arr,nan=-1)#replacing missing values with -1
print("Array after replacing missing values with -1:",arr3)

#we can use np.isinf() function to find the infinite values in the array
arr4=np.array([1,2,np.inf,4,5,-np.inf,7,8,9,10])
infinite_values=np.isinf(arr4)
print("Infinite values:",infinite_values)

#replacing the infinite values with a specified value
arr6=np.nan_to_num(arr4,posinf=100,neginf=-100)#replacing positive infinite values with 100 and negative infinite values with -100
print("Array after replacing infinite values with specified values:",arr6)



'''
NaN: Not a Number, is a special floating-point value used to represent missing or 
undefined data in numerical computations. It is part of the IEEE 754 standard 
for floating-point arithmetic and is commonly used in programming languages and 
libraries that deal with numerical data, such as Python's NumPy library.
NaN is typically used to indicate that a value is not available or cannot be
represented as a valid number. For example, in a dataset, if a measurement is
missing or not applicable, it can be represented as NaN.
NaN has some unique properties:
1. NaN is not equal to any value, including itself. This means that the expression
   NaN == NaN will always evaluate to False.
2. Any arithmetic operation involving NaN will result in NaN. For example,
   NaN + 5 will yield NaN.
3. NaN is considered a floating-point value, so it can only be used with
   floating-point data types.
4. NaN can be generated in various ways, such as dividing zero by zero or taking
   the square root of a negative number.
'''