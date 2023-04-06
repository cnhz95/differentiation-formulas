import numpy as np

def f(x):
    return (np.tan(x)-1.5)

def df(x):
    return (1/(np.cos(x))**2)

def secant(x0, x1):
    return (x1-(f(x1)*(x1-x0))/(f(x1)-f(x0)))

def main():
    x0 = -1.5
    x1 = -1
    print("Secant method")
    for i in range(0, 10):
        x2 = secant(x0, x1)
        err = np.absolute(x1-x2)
        x0 = x1
        x1 = x2
        print(i, x1, err, sep="\t")
    
if __name__ == '__main__':
    main()