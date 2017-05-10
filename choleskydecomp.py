# -*- coding: utf-8 -*-
"""
Created on Wed May 10 01:02:32 2017

@author: Leandro
"""

import numpy as np
from math import sqrt

def C_decomp(A):
    n = len(A)
    L = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1):
            L[i][j] = A[i][j]
            for k in range(j):
                L[i][j] -= L[i][k]*L[j][k]
            if(i == j):
                L[i][j] = sqrt(L[j][j])
            else:
                L[i][j] /= L[j][j]
    return L

def C_forwardsub (L,b):
    n = len(L)
    y = np.copy(b)
    for i in range(1,n):
        for j in range(i):
            y[i] -= L[i][j]*y[j]
        y[i] /= L[i][i]
    return y
            
def C_backwardsub (U,y):
    n = len(U)
    x = np.copy(y)
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            x[i] -= U[j][i]*x[j]
        x[i] /= U[i][i]
    return x
    
def C_solve(L,b):
    y = C_forwardsub(L,b)
    x = C_backwardsub(L,y)
    return x

def C_testex(A, x, b):
    resultado = A.dot(x)
    print("A*x {} = b {} ? {}".format(resultado.round(2), b, resultado.round(2)==b.round(2)))

A = np.array([[1.0,1.0,1.0,1.0],\
              [1.0,4.0,4.0,4.0],\
              [1.0,4.0,9.0,9.0],\
              [1.0,4.0,9.0,18.0]])
b = np.array([1.0,0.0,0.0,0.0])
L = C_decomp(A)
x = C_solve(L,b)
print("Solução:\n x = {}".format(x.round(2)))
#C_testex(A, x, b)
