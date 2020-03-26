from matplotlib import pyplot as plt


import matplotlib
font = {'family' : 'MicroSoft YaHei',
              'weight' : 'bold',
              'size'   : '9'}
matplotlib.rc('font',**font)

y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]


x_3=range(1,32)
x_10=range(51,82)
plt.figure(figsize=(20,8),dpi=80)


plt.scatter(x_3,y_3,label="三月份")
plt.scatter(x_10,y_10,label="十月份")

_x=list(x_3)+list(x_10)
_x_label=[f"3月{i}" for i in x_3]
_x_label+=[f"10月{i-50}" for i in x_10]
plt.xticks(_x[::3],_x_label[::3],rotation=45)

plt.legend()

plt.xlabel("时间")
plt.ylabel("温度")
plt.title("标题")
plt.show()
