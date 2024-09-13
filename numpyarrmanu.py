import  numpy as  np 
arr = np.array([2,4,6,8,10])
v = arr.view()
print("id of arr", id(arr))
print("id  of  v", id(v))

arr[0] = 12

print("orginal array" , arr)
print("view-",v)
