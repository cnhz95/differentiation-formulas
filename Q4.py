import numpy as np
import sympy as sym

def f(x):
    return (np.sqrt((x-5)**5)+2*np.cos(np.pi*np.sqrt(x)))/(np.sqrt(x+4*np.log(x-np.pi))-1)

def main():
    x0 = 7
    h = [0.04, 0.02, 0.01]
    
    D3 = np.zeros(3)
    D3[0] = (f(x0-h[0])-2*f(x0)+f(x0+h[0]))/(h[0]**2)
    D3[1] = (f(x0-h[1])-2*f(x0)+f(x0+h[1]))/(h[1]**2)
    D3[2] = (f(x0-h[2])-2*f(x0)+f(x0+h[2]))/(h[2]**2)
    
    for i in range(len(D3)):
        print(D3[i])

    x = Symbol('x')
    f_sym = (sym.sqrt((x-5)**5)+2*sym.cos(sym.pi*sym.sqrt(x)))/(sym.sqrt(x+4*sym.log(x-sym.pi))-1)
    
    f_prim = diff(f_sym, x)
    f_biss = diff(f_prim, x)
    f_biss_x_0 = f_biss.subs(x, x0)
    
    print(f_biss_x_0.evalf())
    
if __name__ == '__main__':
    main()