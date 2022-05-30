# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:46:26 2022

@author: Asus
"""

import matplotlib.pyplot as plt
import pandas as pd
import Clasification_Algorithm as A
import os
import time
plt.style.use('dark_background')


def clasifier_graphic(folder):
    start = time.time()
    os.mkdir('Clasifications periodic')
    os.mkdir('Clasifications no periodic')
    datos = pd.read_csv('Star informations.csv', low_memory=False)
    maxi = max(datos['period'])
    comprobacion = datos[datos['period'].isnull()]
    os.chdir(folder)
    rute = os.getcwd()
    print(100*'-')
    nv = 0
    t = 0
    v = 0
    e = 0
    for i in os.listdir(rute):
        start2 = time.time()
        try:
            if (i.replace('.dat', '')).replace('-V', '-V ') not in comprobacion['asassn_name'].tolist():
                print('Star: ', (i.replace('.dat', '')).replace('-V', '-V '))
                print('')
                print('The star ', (i.replace('.dat', '')).replace(
                    '-V', '-V '), 'is periodic')
                os.chdir('..')
                os.chdir('Clasifications periodic')
                os.mkdir('Star '+(i.replace('.dat', '')).replace('-V', '-V '))
                os.chdir('Star '+(i.replace('.dat', '')).replace('-V', '-V '))
                aux = os.getcwd()
                os.chdir('..')
                os.chdir('..')
                os.chdir(folder)
                date = A.graphic_information(
                    i, datos, aux, maxi)

                print(date)
                os.chdir('..')
                os.chdir('Clasifications periodic')
                os.chdir('Star '+(i.replace('.dat', '')).replace('-V', '-V '))
                f = open("information "+(i.replace('.dat', '')
                                         ).replace('-V', '-V ')+".txt", "w+")
                f.write(date)
                os.chdir('..')
                os.chdir('..')
                os.chdir(folder)
                t += 1
                v += 1
                print('')
                print('total: ', t)
                print('variables: ', v)
                print('non variables: ', nv)
                print('error: ', e)
                print('The time for this start was '+str(time.time()-start2))
                print('Total time until now: '+str(time.time()-start)+' s')

                print(100*'-')
            else:
                print('Star: ', i.replace('dat', ''))
                print('')
                print('The star ', i.replace('dat', ''), 'is not periodic')
                os.chdir('..')
                os.chdir('Clasifications no periodic')
                f = open("information not periodc stars.txt", "a")
                f.write(i+'\n')
                os.chdir('..')
                os.chdir(folder)
                t += 1
                nv += 1
                print('')
                print('total: ', t)
                print('variables: ', v)
                print('non variables: ', nv)
                print('error: ', e)
                print('The time for this start was '+str(time.time()-start2))
                print('Total time until now: '+str(time.time()-start)+' s')
                print(100*'-')
        except:
            print('')
            print('gatspy error')
            t += 1
            e += 1
            print('')
            print('total: ', t)
            print('variables: ', v)
            print('non variables: ', nv)
            print('error: ', e)
            print('The time for this start was '+str(time.time()-start2))
            print('Total time until now: '+str(time.time()-start)+' s')
            print(100*'-')
    return 'The time used was: '+str(time.time()-start)+' s'


def correr():
    x = input('porfavor ingrese la carpeta a analizar:')
    try:
        print(clasifier_graphic(x))
    except:
        print('La carpeta que desea ya se clasificó o no existe, a continuación ingrese un nombre válido')
        correr()


correr()
