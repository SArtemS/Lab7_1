# Написание программы для численного интегрирования площади под кривой.
def integrate(f, a, b, n_iter=1000):
    h = (b - a) / n_iter
    fsum = 0
    hsum = a + h
    while (hsum < b):
        fsum += f(hsum)
        hsum += h
    res = round(h * ((f(a) + f(b)) / 2 + fsum), 8)
    return(res)
# f - функция (например, sin, cos, tan, ...) # может быть любая функция из библиотеки math
