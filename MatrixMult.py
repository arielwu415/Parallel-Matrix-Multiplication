# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:22:09 2022

@author: Ariel
"""

from mpi4py import MPI
import numpy
import random
import time


def generate_matrix(n):
    matrix = []
    for i in range(0, n):
        matrix.append([random.randint(1, 5) for j in range(0, n)])
    return numpy.array(matrix)

def initialize_matrix(n, m):
    matrix = []
    for i in range(0, n):
        matrix.append([0 for j in range(0, m)])
    return numpy.array(matrix)


### Creating Comm Protocol
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
p = comm.Get_size()
root = 0
n = 100


### Data Assignment
newA = []
newB = []
if rank == root:
    A = generate_matrix(n)
    B = generate_matrix(n)

    # slice matrix A and B into blocks
    for r in range(0, p):
        start = int(r*n/p)
        end = int((r+1)*n/p)
        subA = A[start:end, :]
        subB = B[:, start:end]
        newA.append(subA)
        newB.append(subB)

Ar = comm.scatter(newA, root)
Br = comm.scatter(newB, root)
Brproc = Br
Cr = initialize_matrix(len(Ar), len(Br))


### Step Iteration
start = time.time()
for t in range(0, p):
    SPROC = (rank+t) % p
    RPROC = (rank-t+p) % p
    if t != 0:        
        sreq = comm.Isend(Br, dest=SPROC, tag=SPROC)
        rreq = comm.Irecv(Brproc, source=RPROC, tag=rank)
        sreq.wait()
        rreq.wait()
    
    for i in range(0, int(n/p)):
        for j in range(0, int(n/p)):
            for k in range(0, n):
                Cr[i, j+RPROC*int(n/p)] += Ar[i, k]*Brproc[k, j]


### Gather blocks from processors
C = comm.gather(Cr, root=0)
end = time.time()


### Calculate duration
duration = end - start
time_list = comm.gather(duration, root=0)

if rank == 0:
    time = sum(time_list)
    print(time)

