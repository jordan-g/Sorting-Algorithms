import plotting
import random

# create list to sort
x = [ random.uniform(0, 10) for i in range(100) ]

plotting.set_plot_data(x)

def bubble_sort(x, n):
	if n == 1:
		return

	swapped = False
	for j in range(n-1):
		if x[j+1] < x[j]:
			x[j], x[j+1] = x[j+1], x[j]

			swapped = True

		plotting.set_plot_data(x)

	if not swapped:
		return

	bubble_sort(x, n-1)

bubble_sort(x, len(x))