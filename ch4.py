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

Z_C = 6
Z_H = 1

lim = 5 # First 5 orbitals are for the C atom
n = 9 # There are 9 orbitals inside the basis
# The last 4 orbitals correspond to 1 H atom each

#%% LOAD DATA

os.chdir(path)

P = np.loadtxt("ch4_p.txt")
S = np.loadtxt("ch4_s.txt")
#SP = np.loadtxt("ch4_sp.txt")
#PS = np.loadtxt("ch4_ps.txt")

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

#%% START MULLIKEN'S POPULATION ANALYSIS

#%% Ocupation levels

D = np.matmul(P, S)

levels = np.diag(D)
t = np.sum(levels) # 10 electrons :)

#%% Mülliken Effective Charge

q = np.array([Z_C - np.sum(levels[0:lim]),
              *[Z_H - levels[i] for i in range(lim,n)]])

Q = np.sum(q) # Almost zero. Nice, since it's not polar :)
# They actually fit nicely with Marta's results

#%% Rhos for Effective Charge (definitly not equal to qs)

rho = np.array([np.sum(levels[0:lim]),
                *[levels[i] for i in range(lim,n)]])
    
#%% Bond order. Bond, James Bond (?)

W_C = np.array([np.sum([D[i,j]*D[j,i] 
                for i in range(lim)]) # i runs on C orbitals
                for j in range(lim,n)]) # j runs on all 4 Hs (1 orbital each)

W_Hs = []
for j in range(lim, n): # j runs on all 4 Hs (1 orbital each)
    w = [np.sum([D[j,i]*D[i,j] for i in range(lim)])] # i runs on C orbitals
    for k in range(lim, n): # k runs on the 3 other Hs (1 orbital each)
        if k != j: # do not count each H atom with itself
            w.append(D[j,k]*D[k,j])
    W_Hs.append(np.array(w))
W_Hs = np.array(W_Hs)
del j, k, w

W = np.array([W_C, *W_Hs]) # Pretty close to 1 only on C-H interactions :)
del W_C, W_Hs

#%% Valance indices

V = [np.sum(r) for r in W] # Pretty close to [4,1,1,1,1] :D
# The C has 4 bonds (one to each H)
# And each H has only one bond (to the C atom)