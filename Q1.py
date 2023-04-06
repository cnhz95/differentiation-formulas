import numpy as np

def f(x):
    return (np.sqrt((x-5)**5)+2*np.cos(np.pi*np.sqrt(x)))/(np.sqrt(x+4*np.log(x-np.pi))-1)

def main():
    x0 = 7
    h = [0.04, 0.02, 0.01]
    
    D1, D2 = ([] for i in range(2))
    D1.append((f(x0+h[0])-f(x0))/h[0])
    D1.append((f(x0+h[1])-f(x0))/h[1])
    D1.append((f(x0+h[2])-f(x0))/h[2])
    
    D2.append((f(x0+h[0])-f(x0-h[0]))/(2*h[0]))
    D2.append((f(x0+h[1])-f(x0-h[1]))/(2*h[1]))
    D2.append((f(x0+h[2])-f(x0-h[2]))/(2*h[2]))
    
    for i in range(3):
        print(D1[i])
        print(D2[i])

if __name__ == '__main__':
    main()