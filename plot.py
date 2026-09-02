import matplotlib.pyplot as plt
x=[12,32,19,33,54,11]
y1=[34,56,13,20,14,2]
y2=[43,52,15,21,89,6]
plt.plot(x, y1)
plt.plot(x,y2)
plt.title('Line draft')
plt.xlim(2,89)
plt.ylim(2,89)
plt.xlabel('Times')
plt.ylabel('Matplotib')
plt.legend()
plt.show()