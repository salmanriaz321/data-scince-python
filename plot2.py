import  matplotlib.pyplot as plt
import numpy as np
x=np.arange (1,11,1)
y1=(2*x)+2
y2=(2*x**3)+2
plt.plot(x,y1, label='(2*x)+2')
plt.plot(x,y2, label='(2*x**3)+2')
plt.legend()
plt.show()
