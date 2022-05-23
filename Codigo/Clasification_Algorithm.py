# Do preliminary imports and notebook setup
import os
from gatspy.periodic import LombScargle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('dark_background')


def period_and_amplitude_star(name_of_date_star):
    Data = pd.read_csv(name_of_date_star, delimiter=' ', header=1)
    t = Data['HJD']
    mag = Data['MAG']
    dmag = Data['MAG_ERR']
    model = LombScargle().fit(t, mag, dmag)
    periods, power = model.periodogram_auto(nyquist_factor=100)
    model.optimizer.period_range = (0.1, 1000)
    if (mag-model.predict(t)).sum() > (0.1)*len(Data):
        print('')
        print('Comprobation end, the star is not variable')
        print('')
        return 'Thanks'
    else:
        print('')
        print('Comprobation end, the star is variable')
        print('')
        print('Thanks')
        print('')
        print('Return the T and the A (T,A)')
        period = model.best_period
        amplitude = (abs(np.array(Data['MAG'].tolist()).mean()-abs(max(Data['MAG'])))+abs(
            np.array(Data['MAG'].tolist()).mean()-abs(min(Data['MAG']))))*(1/2)
        return period, amplitude


def graphic_information(name_of_date_star):
    Data = pd.read_csv(name_of_date_star, delimiter=' ', header=1)
    t = Data['HJD']
    mag = Data['MAG']
    dmag = Data['MAG_ERR']
    model = LombScargle().fit(t, mag, dmag)
    periods, power = model.periodogram_auto(nyquist_factor=100)
    model.optimizer.period_range = (0.1, 1000)
    if (mag-model.predict(t)).sum() > (0.1)*len(Data):
        print('')
        print('Comprobation end, the star is not variable')
        print('')
        return 'Thanks'
    else:
        print('')
        Data = pd.read_csv(name_of_date_star, delimiter=' ', header=1)
        t = Data['HJD']
        mag = Data['MAG']
        dmag = Data['MAG_ERR']
        model = LombScargle().fit(t, mag, dmag)
        periods, power = model.periodogram_auto(nyquist_factor=100)
        fig, ax = plt.subplots()
        ax.plot(periods, power)
        ax.set(xlabel='period (days)',
               ylabel='Lomb-Scargle Power')
        ax.set_title('Periodgram '+name_of_date_star)
        plt.show()
        model.optimizer.period_range = (0.1, 1000)
        period = model.best_period
        amplitude = (abs(np.array(Data['MAG'].tolist()).mean()-abs(max(Data['MAG'])))+abs(
            np.array(Data['MAG'].tolist()).mean()-abs(min(Data['MAG']))))*(1/2)
        fig, ax1 = plt.subplots()
        ax1.scatter(Data['HJD'], Data['MAG'])
        ax1.set_title('Experimental dates from '+name_of_date_star)
        ax1.set_xlabel('hjd')
        ax1.set_ylabel('mag')
        plt.show()
        aux = Data['HJD'].tolist()
        fig, ax2 = plt.subplots()
        ax2.scatter(
            np.linspace(aux[0], aux[-1], 100), model.predict(
                np.linspace(aux[0], aux[-1], 100)))
        ax2.set_title('Dates ajusted from '+name_of_date_star +
                      ' trought Lomb-Scargle Power')
        ax2.set_xlabel('hjd')
        ax2.set_ylabel('mag')
        plt.show()
        print('period ajust= ', period)
        print('amplitude ajust = ', amplitude)
        return 'Thanks'
