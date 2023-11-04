#!/usr/bin/env python3

# Import MPI
from mpi4py import MPI

if __name__ == "__main__":

    # Define MPI communicator
    world_comm = MPI.COMM_WORLD

    # Get size of out CPU
    world_size = world_comm.Get_size()

    # Get the ranks (ID of the processors)
    my_rank = world_comm.Get_rank()

    # Print 
    print("World size: " +  str(world_size) + "  " + "Rank: " + str(my_rank))
