import matplotlib.pyplot as plt
import numpy as np

plt.ion()
fig = plt.figure()
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.axis('off')
fig.add_axes(ax)
heatmap = None
plt.show()

def set_plot_data(x):
	global heatmap
	global fig
	global ax

	if type(x) is list:
		x = np.array(x)
	if len(x.shape) == 1:
		x = x[np.newaxis, :]

	if heatmap is None:
		heatmap = ax.imshow(x, aspect='auto')
	else:
		heatmap.set_data(x)
		heatmap.set_clim(vmin=np.amin(x), vmax=np.amax(x))
		heatmap.set_extent((0, x.shape[1], x.shape[0], 0))

	fig.canvas.draw()
	plt.pause(0.001)