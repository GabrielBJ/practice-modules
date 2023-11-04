#!/usr/bin/env python3

# Importing libraries
from mpi4py import MPI
import numpy as np

# Call main to execute the script
if __name__ == '__main__':

    # Define the vector size
    N = 10000000

    # Initialise the first vector
    a = np.ones(N)

    # Initialise the second vector
    b = np.zeros(N)

    # Add values to the second vector
    for i in range(N):
        b[i] = 1.0 + i

    # Add the two arrays
    for i in range(N):
        a[i] = a[i] + b[i]

    # Average the result
    summ = 0.0

    for i in range(N):
        summ += a[i]
    average = summ / N

    # Print the result
    print("Average is: ", average)
