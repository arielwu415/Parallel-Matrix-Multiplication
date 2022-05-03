echo "Running with 1 processor..."
mpiexec -n 1 python MM_100.py
mpiexec mpirun -n 1 python MM_250.py
mpiexec mpirun -n 1 python MM_500.py
mpiexec mpirun -n 1 python MM_1000.py

echo "Running with 2 processors..."
mpiexec mpirun -n 2 python MM_100.py
mpiexec mpirun -n 2 python MM_250.py
mpiexec mpirun -n 2 python MM_500.py
mpiexec mpirun -n 2 python MM_1000.py

echo "Running with 4 processors..."
mpiexec mpirun -n 4 python MM_100.py
mpiexec mpirun -n 4 python MM_250.py
mpiexec mpirun -n 4 python MM_500.py
mpiexec mpirun -n 4 python MM_1000.py

echo "Running with 8 processors..."
mpiexec mpirun -n 8 python MM_100.py
mpiexec mpirun -n 8 python MM_250.py
mpiexec mpirun -n 8 python MM_500.py
mpiexec mpirun -n 8 python MM_1000.py
