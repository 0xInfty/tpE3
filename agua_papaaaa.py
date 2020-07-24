import numpy as np
#%%
P=np.loadtxt('P_agua.txt')
S=np.loadtxt('S_agua.txt')
#%%
S1=np.square(S)
j=np.matmul(S1,P)
D=np.matmul(P,S)
#%%
d=np.loadtxt('s(0.5)Ps(0.5).txt')
#%%
t=np.trace(np.matmul(P,S))
print(t)
#%%
niv=[]
for i in range(7):
    p=D[i,i]
    niv.append(p)
print(niv)
sum=0
for i in range(7):
    sum=sum+niv[i]
print(sum)