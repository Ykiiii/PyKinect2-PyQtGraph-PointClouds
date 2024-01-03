import pyqtgraph.opengl as gl
import numpy as np

# 创建一个OpenGL窗口
app = gl.GLViewWidget()
app.show()

# 创建一个随机的点集

n = 100
pos = np.random.normal(size=(n, 3))
color = np.ones((n, 4))
size = np.random.uniform(5, 10, size=n)

# 使用gl.GLScatterPlotItem方法绘制散点图
scatter = gl.GLScatterPlotItem(pos=pos, color=color, size=size)
app.addItem(scatter)
