import numpy as np
var1=np.linspace(10, 50, 4)
print(var1)

var2 = np.array([(2, 4, 6), (1, 3, 5),(4,6,9),(9,10,14)])
print(var2[0, 1])
print(var2[2:, 1])
print(var2.max())
print(var2.min())
print(var2.sum())