# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:46:26 2022

@author: Asus
"""
from gatspy.periodic import LombScargle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import Clasification_Algorithm as A
import os
plt.style.use('dark_background')


def clasifier(folder):
    current_directory = os.getcwd()
    os.chdir(folder)
    rute = os.getcwd()
    print(100*'-')
    for i in os.listdir(rute):
        print('Star: ', i)
        print(A.period_and_amplitude_star(i))
        print(100*'-')


def clasifier_graphic(folder):
    current_directory = os.getcwd()
    os.chdir(folder)
    rute = os.getcwd()
    print(100*'-')
    for i in os.listdir(rute):
        print('Star: ', i)
        print(A.graphic_information(i))
        print(100*'-')
