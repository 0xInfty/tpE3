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
#%%
q=0
for i in range(5):
    q=q+niv[i]

qo=8-q

qh1=1-niv[5]
qh2=1-niv[6]
print(qo)
print(qh1)
print(qh2)
#%%
W_oh1=[]
for i in range(5):
    ter=D[i,5]*D[5,i]
    W_oh1.append(ter)
W_oh1=np.sum(W_oh1)
print(W_oh1)

W_oh2=[]
for i in range(5):
    ter=D[i,6]*D[6,i]
    W_oh2.append(ter)
W_oh2=np.sum(W_oh2)
print(W_oh2)

W_h1h2=D[5,6]*D[6,5]
print(W_h1h2)
#%%

Vo=W_oh1+W_oh2
Vh=W_oh1+W_h1h2
print(Vo)
print(Vh)




