from gatspy.periodic import LombScargleFast
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('dark_background')


def graphic_information(name_of_date_star, dataset, aux, maxi):
    Data = pd.read_csv(name_of_date_star, delimiter=' ', header=1)
    t = Data['HJD']
    mag = Data['MAG']
    dmag = Data['MAG_ERR']
    model = LombScargleFast().fit(t, mag, dmag)
    periods, power = model.periodogram_auto(nyquist_factor=100)
    print('')
    fig, ax = plt.subplots()
    ax.plot(periods, power)
    ax.set(xlabel='period (days)',
           ylabel='Lomb-Scargle Power')
    ax.set_title('Periodgram '+name_of_date_star)
    plt.savefig(aux+'\\Periodgram')
    try:
        model.optimizer.period_range = (0.1, maxi)
        period = model.best_period
        amplitude = (abs(np.array(Data['MAG'].tolist()).mean()-abs(max(Data['MAG'])))+abs(
            np.array(Data['MAG'].tolist()).mean()-abs(min(Data['MAG']))))*(1/2)
        fig, ax1 = plt.subplots()
        ax1.scatter(Data['HJD'], Data['MAG'])
        ax1.set_title('Experimental dates from '+name_of_date_star)
        ax1.set_xlabel('hjd')
        ax1.set_ylabel('mag')
        plt.savefig(aux+'\\Experimental dates')
        fig, ax2 = plt.subplots()
        ax2.scatter(t, model.predict(t))
        ax2.set_title('Dates ajusted from '+name_of_date_star +
                      ' trought Lomb-Scargle Power')
        ax2.set_xlabel('hjd')
        ax2.set_ylabel('mag')
        plt.savefig(aux+'\\Ajusted dates')
        star = dataset[dataset['asassn_name'] == (
            name_of_date_star.replace('.dat', '')).replace('-V', '-V ')]
        amplitude2 = star['amplitude'].tolist()[0]
        period2 = star['period'].tolist()[0]
        return 'The information found for us is: \n'+'The period is: '+str(period)+' days and the amplitud is '+str(amplitude)+' mag \n'+'The information of the Asassn is: \n'+'The period is: '+str(period2)+' days and the amplitud is '+str(amplitude2)+' mag \n'
    except:
        model.optimizer.period_range = (0.1, len(Data))
        period = model.best_period
        amplitude = (abs(np.array(Data['MAG'].tolist()).mean()-abs(max(Data['MAG'])))+abs(
            np.array(Data['MAG'].tolist()).mean()-abs(min(Data['MAG']))))*(1/2)
        fig, ax1 = plt.subplots()
        ax1.scatter(Data['HJD'], Data['MAG'])
        ax1.set_title('Experimental dates from '+name_of_date_star)
        ax1.set_xlabel('hjd')
        ax1.set_ylabel('mag')
        plt.savefig(aux+'\\Experimental dates')
        fig, ax2 = plt.subplots()
        ax2.scatter(t, model.predict(t))
        ax2.set_title('Dates ajusted from '+name_of_date_star +
                      ' trought Lomb-Scargle Power')
        ax2.set_xlabel('hjd')
        ax2.set_ylabel('mag')
        plt.savefig(aux+'\\Ajusted dates')
        star = dataset[dataset['asassn_name'] == (
            name_of_date_star.replace('.dat', '')).replace('-V', '-V ')]
        amplitude2 = star['amplitude'].tolist()[0]
        period2 = star['period'].tolist()[0]
        return 'The information found for us is: \n'+'The period is: '+str(period)+' days and the amplitud is '+str(amplitude)+' mag \n'+'The information of the Asassn is: \n'+'The period is: '+str(period2)+' days and the amplitud is '+str(amplitude2)+' mag \n'
