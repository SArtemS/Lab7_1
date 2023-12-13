import timeit
from integrate import integrate
from math import sin, cos, tan


if __name__ == '__main__':
    print("Function sin, a = 3, b = 5")
    # python -m timeit -s "from integrate import integrate; from math import sin" "integrate(sin, 3, 5, n_iter=1000)"
    print("Iterations = 1000\tresult = " + str(integrate(sin, 3, 5, 1000)) + "\tat 155 usec per loop")
    # python -m timeit -s "from integrate import integrate; from math import sin" "integrate(sin, 3, 5, n_iter=10000)"
    print("Iterations = 10000\tresult = " + str(integrate(sin, 3, 5, 10000)) + "\tat 1.63 msec per loop")
    # python -m timeit -s "from integrate import integrate; from math import sin" "integrate(sin, 3, 5, n_iter=100000)"
    print("Iterations = 100000\tresult = " + str(integrate(sin, 3, 5, 100000)) + "\tat 15.3 msec per loop")

    print("\nFunction cos, a = 3, b = 5")
    # python -m timeit -s "from integrate import integrate; from math import cos" "integrate(cos, 0, 1, n_iter=1000)"
    print("Iterations = 1000\tresult = " + str(integrate(cos, 3, 5, 1000)) + "\tat 155 usec per loop")
    # python -m timeit -s "from integrate import integrate; from math import cos" "integrate(cos, 0, 1, n_iter=10000)"
    print("Iterations = 10000\tresult = " + str(integrate(cos, 3, 5, 10000)) + "\tat 1.46 msec per loop")
    # python -m timeit -s "from integrate import integrate; from math import cos" "integrate(cos, 0, 1, n_iter=100000)"
    print("Iterations = 100000\tresult = " + str(integrate(cos, 3, 5, 100000)) + "\tat 14.9 msec per loop")

    print("\nFunction tan, a = 3, b = 5")
    # python -m timeit -s "from integrate import integrate; from math import tan" "integrate(tan, 0, 1, n_iter=1000)"
    print("Iterations = 1000\tresult = " + str(integrate(tan, 3, 5, 1000)) + "\tat 154 usec per loop")
    # python -m timeit -s "from integrate import integrate; from math import tan" "integrate(tan, 0, 1, n_iter=10000)"
    print("Iterations = 10000\tresult = " + str(integrate(tan, 3, 5, 10000)) + "\tat 1.66 msec per loop")
    # python -m timeit -s "from integrate import integrate; from math import tan" "integrate(tan, 0, 1, n_iter=100000)"
    print("Iterations = 100000\tresult = " + str(integrate(tan, 3, 5, 100000)) + "\tat 15.3 msec per loop")