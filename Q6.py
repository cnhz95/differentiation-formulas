import numpy as np

def f(x):
    return -(np.cos(x)+x/5)

def df(x):
    return np.sin(x)-1/5

def newton_raphson(x):
    return x-f(x)/df(x)

def main():
    eps = [0.5e-7, 0.9e-8, 0.5e-9, 0.7e-10, 0.5e-12, 0.7e-14]
    for e in eps:
        x, n = 1, 0
        while np.absolute(f(x)/df(x)) > e:
            x = newton_raphson(x)
            n = n + 1
        print(f"Nollstället {x} hittades efter {n} iteratoner med toleransen {e}")

if __name__ == '__main__':
    main()