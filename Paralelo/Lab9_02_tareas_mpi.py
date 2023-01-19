#=======================================
# mpirun -n 4 python3 tareas_mpi.py
#=======================================
from mpi4py import MPI

#=========================
# Objeto de comunicadores
#=========================
comm = MPI.COMM_WORLD

#=========================
# Cuantos somos en total
#=========================
size = comm.Get_size()

#==============
# Quien soy
#==============
rank = comm.Get_rank()

#=============================
# Si yo soy el cero hago esto
#=============================
if rank == 0:
    print("Yo soy el proceso cero")

#=================================
# Si yo soy el uno hago esto otro
#=================================
elif rank == 1:
    print("Yo soy el proceso uno")

#===============================================
# Si yo no soy ni el uno ni el cero, hago esto
#===============================================
else:
    print("Yo no soy ninguno de los dos primeros procesos")

print("Reportandome, soy el proceso ", str(rank), "de", str(size))

