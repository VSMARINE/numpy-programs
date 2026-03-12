#we are going to filter out data based on some conditions
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
#we will filter out even numbers from this array
even_numbers=arr[arr%2==0]
print("Even numbers:",even_numbers)
#we will filter out odd numbers from this array
odd_numbers=arr[arr%2!=0]
print("Odd numbers:",odd_numbers)
#we will filter out numbers greater than 5 from this array
greater_than_five=arr[arr>5]
print("Numbers greater than 5:",greater_than_five)

arr2=arr[arr-2]
print("Array after adding 2 to each element:",arr2)