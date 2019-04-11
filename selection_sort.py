import plotting
import random

# create list to sort
x = [ random.uniform(0, 10) for i in range(100) ]

plotting.set_plot_data(x)

for i in range(len(x)):
	# get index of minimum element from i onwards
	min_index = i
	for j in range(i, len(x)):
		if x[j] < x[min_index]:
			min_index = j

	# swap with the element at index i
	x[i], x[min_index] = x[min_index], x[i]

	plotting.set_plot_data(x)