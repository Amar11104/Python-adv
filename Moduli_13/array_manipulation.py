import numpy as np

arr_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)

element = arr_2d[1,2]
print(element)

dimensions = arr_2d.ndim
print(dimensions)

print(arr_2d.shape)
print(arr_2d.size)

sub_array = arr_2d[:2,:2]
print(sub_array)

sum_rows = np.sum(arr_2d, axis=1)
print(sum_rows)