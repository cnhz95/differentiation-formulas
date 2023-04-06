import numpy as np
import sympy as sym

def main():
    x = sym.Symbol('x')
    f = (sym.sqrt((x-5)**5)+2*sym.cos(sym.pi*sym.sqrt(x)))/(sym.sqrt(x+4*sym.log(x-sym.pi))-1)
    
    x0 = 7
    f_prim = sym.diff(f)
    f_prim_x_0 = f_prim.subs(x, x0)
    
    
    print(f_prim_x_0.evalf())

if __name__ == '__main__':
    main()