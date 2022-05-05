echo "Running with 1 processor..."
mpiexec -n 1 python MM_100.py
mpiexec -n 1 python MM_250.py
mpiexec -n 1 python MM_500.py
mpiexec -n 1 python MM_1000.py

echo "Running with 2 processors..."
mpiexec -n 2 python MM_100.py
mpiexec -n 2 python MM_250.py
mpiexec -n 2 python MM_500.py
mpiexec -n 2 python MM_1000.py

echo "Running with 4 processors..."
mpiexec -n 4 python MM_100.py
mpiexec -n 4 python MM_250.py
mpiexec -n 4 python MM_500.py
mpiexec -n 4 python MM_1000.py

echo "Running with 8 processors..."
mpiexec -n 8 python MM_100.py
mpiexec -n 8 python MM_250.py
mpiexec -n 8 python MM_500.py
mpiexec -n 8 python MM_1000.py
