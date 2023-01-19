from multiprocessing import Process, Pipe

def f(extremo):
    extremo.send([0,1,2,3,4])
    extremo.close()


