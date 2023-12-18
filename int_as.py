from concurrent.futures import as_completed, ThreadPoolExecutor
from functools import partial


def integrate(f, a, b, n_iter):
    h = (b - a) / n_iter
    fsum = 0
    hsum = a + h
    while (hsum < b):
        fsum += f(hsum)
        hsum += h
    res = round(h * ((f(a) + f(b)) / 2 + fsum), 8)
    return (round(res, 4))


def integrate_async(f, a, b, n_iter, n_jobs):
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        step = (b - a) / n_jobs
        fs = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
        
        spawn_lst = []
        for i in fs:
            spawn = partial(executor.submit, integrate, f, i[0], i[1],
                            n_iter // n_jobs)
            spawn_lst.append(spawn)
            
        res = []
        for f in spawn_lst:
            res.append(f())

        s = [r.result() for r in as_completed(res)]
        return round(sum(s), 4)
