from functions import *
import random

# create list to sort
x = [ random.uniform(0, 10) for i in range(100) ]

insertion_sort(x, plot=True)

# create list to search through
x = [ i for i in range(1000) ]

binary_search(x, 64, plot=True)