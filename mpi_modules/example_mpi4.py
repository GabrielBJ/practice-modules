#!/usr/bin/env python3

# Importing libraries
from mpi4py import MPI
import numpy as np

# Call the main to execute the script

if __name__ == "__main__":

    # Define our communicator for MPI
    world_comm = MPI.COMM_WORLD

    # Get size of our CPU
    world_size = world_comm.Get_size()

    # Get the ranks (ID for the processors)
    my_rank = world_comm.Get_rank()

    # Define a vector size
    N = 10000000

    # Add an init time stamp
    start_time_a = MPI.Wtime()

    # Initialise the first vector
    a = np.ones(N)

    # Add an end time stamp
    end_time_a = MPI.Wtime()
    
    # Print the a time stamp
    if my_rank == 0:
        print("Initialise a time: " + str(end_time_a - start_time_a))

    # Initialise the second vector
    b = np.zeros(N)

    # Add values to the second vector
    for i in range(N):
        b[i] = 1.0 + i

    # Add the two vectors
    for i in range(N):
        a[i] = a[i] + b[i]

    # Average the result
    summ = 0.0

    # for loop
    for i in range(N):
        summ += a[i]
    
    average = summ / N

    # Print result
    if my_rank == 0:
        print("Average: " + str(average))
