import numpy as  np
dt  = np.dtype([('name' , np.unicode_, 16), ('grades',np.float64,(2,))])
x = np.array([('Sarah',(8.0,7.0)), ('John',(6.0,7.0))], dtype=dt)
print(x[1])
print('Grades of  John are:', x[1]['grades'] )
print("names are :" , x['name'])