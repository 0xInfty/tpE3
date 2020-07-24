# -*- coding: utf-8 -*-
"""
TP ESTRUCTURA DE LA MATERIA 3
1er cuatrimestre 2020
-------------------------------
EJERCICIO 1: Metano

@author: Leandro Fernandez, Valeria Pais
"""

import os as os
import numpy as np

#%% VARIABLES

path = r"D:\Vall\Documentos\Mis documentos\Facu\Estructura de la Materia 3\TP\tpE3"

Q1 = 6 - 3*1.028 - 1.188 - 1.992
Q2 = 1 - 0.9343

Z_C = 6
Z_H = 1

lim = 5
n = 9

#%% LOAD DATA

os.chdir(path)

P = np.loadtxt("ch4_p.txt")
S = np.loadtxt("ch4_s.txt")
SP = np.loadtxt("ch4_sp.txt")
PS = np.loadtxt("ch4_ps.txt")

#%% VERIFY DATA

# Verify: is P symmetric?
for i in range(9):
    for j in range(9):
        if P[i,j] != P[j,i]:
            print("No es simétrica en", i, j)
del i,j
            
# Verify: is S symmetric?
for i in range(9):
    for j in range(9):
        if S[i,j] != S[j,i]:
            print("No es simétrica en", i, j)
del i,j

#%% Ocupation levels

D = np.matmul(P, S)

niv = np.diag(D)
t = np.sum(niv) # 10 electrones :)

#%% Mülliken Effective Charge

q = np.array([Z_C - np.sum(niv[0:lim]),
              *[Z_H - niv[i] for i in range(lim,n)]])

Q = np.sum(q) # Casi cero. Bien, porque es no polar :)

#%% Rhos for Effective Charge (definitly not equal to qs)

rho = np.array([np.sum(niv[0:lim]),
                *[np.sum(niv[i]) for i in range(lim,n)]])

#rho = np.array([np.sum(D[0:lim,:]),
#                *[np.sum(D[i,:]) for i in range(lim,n)]])

    