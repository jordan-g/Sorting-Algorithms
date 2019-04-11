from functions import *
import random

# create list to sort
x = [ random.uniform(0, 10) for i in range(100) ]

insertion_sort(x, plot=True)