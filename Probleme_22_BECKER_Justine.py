from math import*
import numpy as np

def ouvre():
    fichier=open('C:/Users/Justi/OneDrive/Documents/Mines Nancy/Informatique/p022_names.txt', 'r')
    L=[]
    for line in fichier.readlines():
            L+=line.split('","')
    L[0]='MARY'
    L[-1]='ALONSO'
    return L
    

def convertionalpha(mot):
    S=[]
    M=mot
    Somme=0
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for k in range(len(M)):
        i,j=0,False
        while j==False:
            if M[k]==alphabet[i]:
                j=True
                S.append(i+1)
            i+=1
    for i in range(len(S)):
        Somme+=S[i]
    return Somme


def solve():
    L=ouvre()
    L=sorted(L)
    S=0
    for i in range(len(L)):
        X=convertionalpha(L[i])
        S+=(X*(i+1))
    return S
    
print(solve())
    
    
