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

def binary_search(x, e, l=None, r=None, plot=False):
	# return the index of element e in x[l:r+1] (or -1 if e is not in x)
	# where x is a sorted array

	if r is None:
		r = len(x)

	if l is None:
		l = 0

	if r < l or len(x) == 0:
		return -1

	# set index of middle element
	mid = l + (r - l)//2

	if x[mid] == e:
		return mid

	if plot:
		search_array = [ 0 for i in range(0, l) ] + [ 1 for i in range(l, r+1) ] + [ 0 for i in range(r+1, len(x)) ]
		plotting.set_plot_data(search_array, pause=0.5)

	if x[mid] > e:
		return binary_search(x, e, l, mid-1, plot=plot)
	else:
		return binary_search(x, e, mid+1, r, plot=plot)