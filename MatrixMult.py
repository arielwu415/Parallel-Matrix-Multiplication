# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:22:09 2022

@author: Ariel
"""

from mpi4py import MPI
import numpy
import time

root = 0
n = 6

### Creating Comm Protocol
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
p = comm.Get_size()


### Calculating Num of Rows(Columns) in Each Proc
mod = n%p
n_in_proc = [int(n/p) for i in range(0, p)]
for rem in range(mod):
    n_in_proc[rem] += 1
    

### Generating Sub-Matrices
Ar = numpy.random.randint(5, size=n_in_proc[rank]*n).reshape(n_in_proc[rank], n)
Br = numpy.random.randint(5, size=n_in_proc[rank]*n).reshape(n, n_in_proc[rank])
Brproc = Br
Cr = numpy.zeros([n_in_proc[rank], n], dtype=int)


print(" ", rank, "Ar\n", Ar)
print(" ", rank, "Br\n", Br)
print(" ", rank, "Cr\n", Cr)
print()


### Step Iteration
start = time.time()
for t in range(0, p):
    print()
    SPROC = (rank+t) % p
    RPROC = (rank-t+p) % p
    #ORIGIN = (rank-t+p) % p
    
    if t != 0:
        Brproc = numpy.zeros([n, n_in_proc[RPROC]], dtype=int)
        sreq = comm.Isend(Br, dest=SPROC, tag=SPROC)
        rreq = comm.Irecv(Brproc, source=RPROC, tag=rank)
        sreq.wait()
        rreq.wait()
        
        #print("At", rank, "Ar\n", Ar)
        #print()
        #print(rank, "received Brproc from", RPROC, "size =", n_in_proc[RPROC],"\n", Brproc)
        
    for i in range(0, n_in_proc[rank]):
        for j in range(0, n_in_proc[RPROC]):
            for k in range(0, n):
                location = RPROC*n_in_proc[RPROC]
                # print("Current rank:", rank, "Brproc from", RPROC, "; location =", location)
                # print("t =", t, "; i =", i, "; k =", k, "; j =", j, "; n_in_proc[RPROC] =", n_in_proc[RPROC])
                Cr[i, j+location] += Ar[i, k]*Brproc[k, j]
                #print(Cr)
            


### Gather blocks from processors
C = comm.gather(Cr, root=0)
end = time.time()


### Calculate duration
duration = end - start
time_list = comm.gather(duration, root=0)

if rank == 0:
    time = max(time_list)
    print(time)
    print(C)
