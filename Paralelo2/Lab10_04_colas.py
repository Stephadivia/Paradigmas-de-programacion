from multiprocessing import Process, Queue
def cuadrado(x,q):
    q.put((x,x*x))


