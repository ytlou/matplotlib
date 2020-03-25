#温度10 dian dao 12 dian

from matplotlib import pyplot as plt
import random

import matplotlib
font = {'family' : 'MicroSoft YaHei',
              'weight' : 'bold',
              'size'   : '9'}
matplotlib.rc('font',**font)


a = [random.randint(20,35) for i in range(120)]

x = range(0,120)
y=a
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y)




_xticks_labels = [f"10点{i}分" for i in range(60)]
_xticks_labels += [f"11点{i}分" for i in range(60)]
plt.xticks(list(x)[::3],_xticks_labels[::3],rotation=45)

plt.xlabel("时间")
plt.ylabel("温度")
plt.title("温度变化")

plt.show()
