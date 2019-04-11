import plotting
import random

# create list to sort
x = [ random.uniform(0, 10) for i in range(100) ]

plotting.set_plot_data(x)

for i in range(len(x)-1):
	swapped = False
	for j in range(len(x)-i-1):
		if x[j+1] < x[j]:
			x[j], x[j+1] = x[j+1], x[j]

			swapped = True

		plotting.set_plot_data(x)

	if not swapped:
		break