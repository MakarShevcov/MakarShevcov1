import numpy as np
l = np.random.rand(120)
suml = l.sum()
stdl = l.std()
sredl = suml/l.shape[0]
print(suml)
print(stdl)
print(sredl)
