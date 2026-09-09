import matplotlib.pyplot as plt
hight_men=[163,171,173,178,180,181]
hight_women=[149,156,160,164,166,168]
type=[hight_men,hight_women]
label=['hight men', 'hight women']
color=['g','r']
bins=[140,150,170,180,190]
plt.xlabel('hight of man')
plt.ylabel('hight of women')
plt.hist(type,bins,label=label,color=color,width=2)
plt.title("hight of man and women")
plt.legend()
plt.show()