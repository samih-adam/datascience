import datetime; import numpy
import numpy as np 
my_list = [1,2,3]
arr = np.array(my_list)

print(arr)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]
np.array(my_mat)
print(np.array(my_mat))

#building a numpy array easily
#np.arange!!! Amazing

np.arange(0,10)
print(np.arange(0,10))

np.arange(0,11,2)
print(np.arange(0,11,2))

#another function that you can use, is np.zeros
np.zeros(3)
print(np.zeros(3))

# youc an also choose the number of zeros you want, and than the collums that you want filled with zeros as well
np.zeros((5,5))
print(np.zeros((5,5)))

np.zeros((2,10))
print(np.zeros((2,10)))

np.ones((5,5))
print(np.ones((5,5)))


np.linspace(0,5,10)

print(np.linspace(0,5,10))