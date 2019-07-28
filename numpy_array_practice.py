import numpy as np

#Create a Numpy Array from a List

lst=[10,20,30,40]
np_arr=np.array(lst)

#add 10 to the Array
np_added=np_arr+10
print(np_added)

list3=[[1,2,3,4],[10,20,30,40],[100,200,300,400]]

np_arr1=np.array(list3,dtype='float')

#print(np_arr1)

#create a 2d array with 3 rows and 4 columns
list2=[[1,2,3,4],[3,4,5,6],[5,6,7,8]]
arr2=np.array(list2)

print(arr2.shape)
