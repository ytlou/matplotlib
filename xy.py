from matplotlib import pyplot as plt


fig = plt.figure(figsize=(20,8),dpi=80)

x = range(2,26,2)


y= [15,13,14.5,17,20,25,26,26,24,22,18,15]

plt.plot(x,y)

#plt.xticks(x)
#plt.xticks(range(0,25))
#plt.xticks(range(0,25))
#plt.xticks(range(0,25,0.5))range  不能0.5

_xticks_labels =[i/2 for i in range(4,49) ]
#plt.xticks(_xticks_labels)

#太长可以取列表步长
plt.xticks(_xticks_labels[::2])
plt.yticks(range(min(y),max(y)+1))


#plt.savefig("./sig_size.png")
#plt.savefig("./sig_size.svg")
plt.show()
