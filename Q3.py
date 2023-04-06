import numpy as np

def f(x):
    return (np.sqrt((x-5)**5)+2*np.cos(np.pi*np.sqrt(x)))/(np.sqrt(x+4*np.log(x-np.pi))-1)

def k(x, h):
    return (2*(2*f(x+h/2)-f(x+h)-f(x))/h**2)
    
def main():
    x0 = 7
    h = 0.02
    k1 = k(x0, h)
    f_prime = (f(x0+h)-f(x0))/h+(k1*h)

    print(f_prime)
    
if __name__ == '__main__':
    main()