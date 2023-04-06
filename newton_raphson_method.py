import numpy as np

def f(x):
    return (np.tan(x)-1.5)

def df(x):
    return (1/(np.cos(x))**2)

def newton_raphson(x):
    return (x-(f(x)/df(x)))

def main():
    x = -1.25
    print("Newton-Raphson Method")
    for i in range(0, 10):
        h = newton_raphson(x)
        err = np.absolute(x-h)
        x = h
        print(i, x, err, sep="\t")

if __name__ == '__main__':
    main()