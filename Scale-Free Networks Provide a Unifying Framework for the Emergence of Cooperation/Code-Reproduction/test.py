import networkx as nx             #导入networkx包
import matplotlib.pyplot as plt
G = nx.watts_strogatz_graph(10,4,0)   #生成一个BA无标度网络G
nx.draw(G)                               #绘制网络G
plt.savefig("ba.png")           #输出方式1: 将图像存为一个png格式的图片文件
plt.show()