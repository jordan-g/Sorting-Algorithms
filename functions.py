import plotting

def selection_sort(x, plot=False):
	if plot:
		plotting.set_plot_data(x)

	for i in range(len(x)):
		# get index of minimum element from i onwards
		min_index = i
		for j in range(i, len(x)):
			if x[j] < x[min_index]:
				min_index = j

		# swap with the element at index i
		x[i], x[min_index] = x[min_index], x[i]

		if plot:
			plotting.set_plot_data(x)

	return x

def bubble_sort(x, plot=False):
	if plot:
		plotting.set_plot_data(x)

	for i in range(len(x)-1):
		swapped = False
		for j in range(len(x)-i-1):
			if x[j+1] < x[j]:
				x[j], x[j+1] = x[j+1], x[j]

				swapped = True

			if plot:
				plotting.set_plot_data(x)

		if not swapped:
			break

	return x

def recursive_bubble_sort(x, plot=False):
	if plot:
		plotting.set_plot_data(x)

	def bubble_sort(x, n):
		if n == 1:
			return

		swapped = False
		for j in range(n-1):
			if x[j+1] < x[j]:
				x[j], x[j+1] = x[j+1], x[j]

				swapped = True

			if plot:
				plotting.set_plot_data(x)

		if not swapped:
			return

		bubble_sort(x, n-1)

	bubble_sort(x, len(x))

	return x

def insertion_sort(x, plot=False):
	if plot:
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

		if plot:
			plotting.set_plot_data(x)

	return x