import numpy as np

def f(x):
    return -(np.cos(x)+x/5)

def secant(x0, x1):
    return x1-((x1-x0)*f(x1))/(f(x1)-f(x0))
    
def main():
    eps = [0.5e-7, 0.9e-8, 0.5e-9, 0.7e-10, 0.5e-12, 0.7e-14]
    for e in eps:
        x0, x1, n = 2, 3, 0
        while np.absolute(x1-x0) > e:
            x2 = secant(x0, x1)
            x0, x1 = x1, x2
            n = n+1
        print(f"Nollstället {x1} hittades efter {n} iterationer med toleransen {e}")
        
if __name__ == '__main__':
    main()