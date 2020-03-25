
from matplotlib import pyplot as plt
import matplotlib
font = {'family' : 'MicroSoft YaHei',
              'weight' : 'bold',
              'size'   : '9'}
matplotlib.rc('font',**font)
x=range(10,30)
y=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2=[1,0,1,4,3,2,3,4,5,4,3,4,5,6,1,2,3,1,1,1]
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y,label="同桌",color="orange",linestyle=":")
plt.plot(x,y2,label = "自己",color ="cyan",linestyle="--")
_xlabel=[f"{i}岁" for i in x]
_ylabel=[f"{i}次" for i in range(7)]
plt.xticks(x,_xlabel,rotation=45)
plt.yticks(range(min(y),max(y)),_ylabel)
plt.grid(alpha = 0.4)
plt.legend(loc="upper left")
plt.show()
