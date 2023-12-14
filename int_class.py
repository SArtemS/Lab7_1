import threading
from threading import Lock


class IntegrateThread(threading.Thread):
    def __init__(self, f, a, b, n_iter):
        super().__init__()
        self._value = 0
        self._f = f
        self._a = a
        self._b = b
        self._n_iter = n_iter
        self._lock = Lock()
        
    def integrate(self):
        h = (self._b - self._a) / self._n_iter
        fsum = 0
        hsum = self._a + h
        while (hsum < self._b):
            fsum += self._f(hsum)
            hsum += h
        res = round(h * ((self._f(self._a) + self._f(self._b)) / 2 + fsum), 8)
        return(round(res, 4))
    
    def integrateThreads(self, threads):
        h = (self._b - self._a) / threads
        n_iter = self._n_iter // threads
        threadlist = []
        res = 0
        for i in range(threads):
            a = self._a + h * i
            b = a + h
            t = IntegrateThread(self._f, a, b, n_iter)
            t.start()
            threadlist.append(t)
        for i in threadlist:
            i.join()
            res += i.get()
        return (round(res, 4))
    
    def run(self):
        self._lock.acquire()
        self._value = self.integrate()
        self._lock.release()
    
    def get(self):
        return self._value   
    