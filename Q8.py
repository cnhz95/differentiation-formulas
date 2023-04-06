import numpy as np
from scipy.optimize import root

def main():
    x0 = [-1, 1, 5]
    sol = root(lambda x: -np.cos(x)-0.2*x, x0)
    print(sol.x)

if __name__ == '__main__':
    main()