from int_class import IntegrateThread
from math import sin, cos, tan, atan, pi
from timeit import timeit

if __name__ == '__main__':
    sin100000 = IntegrateThread(sin, 3, 5, 100000)
    cos100000 = IntegrateThread(cos, 3, 5, 100000)
    tan100000 = IntegrateThread(tan, 3, 5, 100000)
    atan100000 = IntegrateThread(atan, 0, pi / 2, 100000)
    
    print("Function (sin, a = 3, b = 5, iterations = 100000) = " + str(sin100000.integrate()))
    print("Time = " + str(round(timeit("sin100000 = IntegrateThread(math.sin, 3, 5, 100000)\nsin100000.integrate()", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))
    
    print("Function (sin, a = 3, b = 5, iterations = 100000, 2 threads) = " + str(sin100000.integrateThreads(2)))
    print("Time = " + str(round(timeit("sin100000 = IntegrateThread(math.sin, 3, 5, 100000)\nsin100000.integrateThreads(2)", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))
    
    print("Function (sin, a = 3, b = 5, iterations = 100000, 4 threads) = " + str(sin100000.integrateThreads(4)))
    print("Time = " + str(round(timeit("sin100000 = IntegrateThread(math.sin, 3, 5, 100000)\nsin100000.integrateThreads(4)", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))
    
    print("\nFunction (cos, a = 3, b = 5, iterations = 100000) = " + str(cos100000.integrate()))
    print("Time = " + str(round(timeit("cos100000 = IntegrateThread(math.cos, 3, 5, 100000)\ncos100000.integrate()", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))
    
    print("Function (cos, a = 3, b = 5, iterations = 100000, 2 threads) = " + str(cos100000.integrateThreads(2)))
    print("Time = " + str(round(timeit("cos100000 = IntegrateThread(math.cos, 3, 5, 100000)\ncos100000.integrateThreads(2)", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))
    
    print("Function (cos, a = 3, b = 5, iterations = 100000, 4 threads) = " + str(cos100000.integrateThreads(4)))
    print("Time = " + str(round(timeit("cos100000 = IntegrateThread(math.cos, 3, 5, 100000)\ncos100000.integrateThreads(4)", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))
    
    print("\nFunction (tan, a = 3, b = 5, iterations = 100000) = " + str(tan100000.integrate()))
    print("Time = " + str(round(timeit("tan100000 = IntegrateThread(math.tan, 3, 5, 100000)\ntan100000.integrate()", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))
    
    print("Function (tan, a = 3, b = 5, iterations = 100000, 2 threads) = " + str(tan100000.integrateThreads(2)))
    print("Time = " + str(round(timeit("tan100000 = IntegrateThread(math.tan, 3, 5, 100000)\ntan100000.integrateThreads(2)", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))

    print("Function (tan, a = 3, b = 5, iterations = 100000, 4 threads) = " + str(tan100000.integrateThreads(4)))
    print("Time = " + str(round(timeit("tan100000 = IntegrateThread(math.tan, 3, 5, 100000)\ntan100000.integrateThreads(4)", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))
   
    print("\nFunction (atan, a = 0, b = pi/2, iterations = 100000) = " + str(atan100000.integrate()))
    print("Time = " + str(round(timeit("atan100000 = IntegrateThread(math.atan, 0, math.pi, 100000)\natan100000.integrate()", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))
    
    print("Function (tan, a = 0, b = pi/2, iterations = 100000, 2 threads) = " + str(atan100000.integrateThreads(2)))
    print("Time = " + str(round(timeit("atan100000 = IntegrateThread(math.atan, 0, math.pi, 100000)\natan100000.integrateThreads(2)", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))

    print("Function (tan, a = 0, b = pi/2, iterations = 100000, 4 threads) = " + str(atan100000.integrateThreads(4)))
    print("Time = " + str(round(timeit("atan100000 = IntegrateThread(math.atan, 0, math.pi, 100000)\natan100000.integrateThreads(4)", setup="from int_class import IntegrateThread\nimport math", number=10), 4)))
