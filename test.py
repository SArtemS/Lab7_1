#  обычный мьютекс, используется для обеспечения 
# эксклюзивного доступа к разделяемому состоянию. 
import threading

from threading import Thread, Lock
import time

class SharedCounter:

    
    def __init__(self, value):
        self._value = value
        self._lock = Lock()
        
    def increment(self, delta=1):
        self._lock.acquire() # захват примитива
        time.sleep(2)
        self._value += delta # 
        time.sleep(2)
        self._lock.release() # освобождение примитива   
        
    def get(self):
        return self._value
    
        
        
sc = SharedCounter(10)

t1 = threading.Thread(target=sc.increment() )
t1.start()
print(sc.get())
t2 = threading.Thread(target=sc.increment() )
t2.start()
print(sc.get())