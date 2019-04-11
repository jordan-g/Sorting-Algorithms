import plotting
import random

# create list to sort
x = [ random.uniform(0, 10) for i in range(100) ]

plotting.set_plot_data(x)

for i in range(1, len(x)):
	# copy element at i
	e = x[i]

	# move all elements before i that are greater than e one index forward
	j = i - 1
	while j >= 0 and x[j] > e:
		x[j+1] = x[j]

		j -= 1

	# element at j is smaller or equal to e, so we stop here and insert e at j+1
	x[j+1] = e

	plotting.set_plot_data(x)