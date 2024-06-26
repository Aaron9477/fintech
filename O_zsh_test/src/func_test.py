import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.signal


array = [0, 1, 2, 3, 1, 4, 3, 2, 3, 2, 8]
array = np.array(array)
array = array + np.random.rand(len(array)) * 0.001
print(array)
order = 4

extres_max =scipy.signal.argrelextrema(array, np.greater, axis=0, order=order, mode='clip')
extres_min =scipy.signal.argrelextrema(array, np.less, axis=0, order=order, mode='clip')

print(extres_max)
print(extres_min)