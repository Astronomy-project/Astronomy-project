# Do preliminary imports and notebook setup
from gatspy.periodic import LombScargle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def comprobation(name_of_date_star):
    validate = None
    Data = pd.read_csv(name_of_date_star)
    t = Data['hjd']
    mag = Data['mag']
    dmag = Data['mag_err']
    model = LombScargle().fit(t, mag, dmag)
    periods, power = model.periodogram_auto(nyquist_factor=100)
    model.optimizer.period_range = (0.1, 1000)
    if (mag-model.predict(t)).sum() > (0.1)*len(Data):
        validate = False
    else:
        validate = True

    return validate


def period_and_amplitude_star(name_of_date_star):

    if comprobation(name_of_date_star) == True:
        Data = pd.read_csv(name_of_date_star)
        t = Data['hjd']
        mag = Data['mag']
        dmag = Data['mag_err']
        model = LombScargle().fit(t, mag, dmag)
        periods, power = model.periodogram_auto(nyquist_factor=100)
        model.optimizer.period_range = (0.1, 1000)
        period = model.best_period
        amplitude = (abs(np.array(Data['mag'].tolist()).mean()-abs(max(Data['mag'])))+abs(
            np.array(Data['mag'].tolist()).mean()-abs(min(Data['mag']))))*(1/2)
        return period, amplitude
    else:
        return 'The star is not variable, please enter a new date star'


def graphic_information(name_of_date_star):
    if comprobation(name_of_date_star) == True:
        Data = pd.read_csv(name_of_date_star)
        t = Data['hjd']
        mag = Data['mag']
        dmag = Data['mag_err']
        model = LombScargle().fit(t, mag, dmag)
        periods, power = model.periodogram_auto(nyquist_factor=100)
        fig, ax = plt.subplots()
        ax.plot(periods, power)
        ax.set(xlabel='period (days)',
               ylabel='Lomb-Scargle Power')
        ax.set_title('Periodgram')
        plt.show()
        model.optimizer.period_range = (0.1, 1000)
        period = model.best_period
        amplitude = (abs(np.array(Data['mag'].tolist()).mean()-abs(max(Data['mag'])))+abs(
            np.array(Data['mag'].tolist()).mean()-abs(min(Data['mag']))))*(1/2)
        fig, ax1 = plt.subplots()
        ax1.scatter(Data['hjd'], Data['mag'])
        ax1.set_title('Experimental dates from'+name_of_date_star)
        ax1.set_xlabel('hjd')
        ax1.set_ylabel('mag')
        plt.show()
        fig, ax2 = plt.subplots()
        ax2.scatter(Data['hjd'], model.predict(Data['hjd']))
        ax2.set_title('Dates ajusted from '+name_of_date_star +
                      'trought Lomb-Scargle Power')
        ax2.set_xlabel('hjd')
        ax2.set_ylabel('mag')
        plt.show()
        print('period ajust= ', period)
        print('amplitude ajust = ', amplitude)
    else:
        return 'The star is not variable, please enter a new date star'
