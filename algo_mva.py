#####################################################
#              Auther : hatem ben tayeb             #
#              Email : hatemtayeb2@gmail.com        #
#              Script : algoritme MVA               #
#              Subjet : evaluation de performance   #
#####################################################

#function MVA
#arguments :
#            N : nombre de sessions clientelle
#            Sm: latence mayenne induit par l'etage m
#            Vm: ratio de viste pour l'etage m
#            Z : think time
#            m : nombre d'etage dans l'application

import numpy as np

M = 20
Sm = [np.random.poisson(6) for i in range(0,M)]
Vm = [np.random.poisson(6) for i in range(0,M)]
N  = 10
Z  =0.01
def __MVA__(N,Sm,Vm,Z):

    """
               algorithme MVA

    :param m: nombre d'etage dans l'application
    :param N: nombre de sessions clientelle
    :param Sm: latence mayenne induit par l'etage m
    :param Vm: ratio de viste pour l'etage m
    :param Z: think time
    :return:
    """

    # nombre d'etage dans l'application

    Rm=[0 for i in range(0,M)]
    Dm=[0 for i in range(0,M)]
    Lm=[0 for i in range(0,M)]
    Lm[0]=0
    Rm[0]=Z
    Dm[0]=Z
    #assert(m<=M)
    for m in range(0, M):
        Lm[m]=0
        Dm[m]=Vm[m]*Sm[m]


    for n in range(1,N):
        for m in range(1,M):
            Rm[m]=Dm[m]*(1+Lm[m])

        taux = n/(Rm[0]+sum(Rm[1:])) #debit



        for m in range(1, M ):
            Lm[m]=taux*Rm[m]  #loi de littel


        Lm[0]=taux*Rm[0]



    R=sum(Rm) # temps de reponse moyen

    return (R,Rm)


print(__MVA__(N,Sm,Vm,Z))