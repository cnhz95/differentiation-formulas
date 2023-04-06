import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return -(np.cos(x)+(x/5))

def main():
    x = np.arange(-10, 10, 0.01)
    y = np.zeros(len(x))
    
    for i in range(len(x)):
        y[i] = f(x[i])
   
    plt.plot(x, y, 'b')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()