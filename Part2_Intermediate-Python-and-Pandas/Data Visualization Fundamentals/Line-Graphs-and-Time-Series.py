import matplotlib.pyplot as plt
import pandas as pd

who_time_series=pd.read_csv('./WHO_time_series.csv')

france = who_time_series[who_time_series['Country'] == 'France']
uk = who_time_series[who_time_series['Country'] == 'The United Kingdom']
italy = who_time_series[who_time_series['Country'] == 'Italy']

plt.plot(france['Date_reported'],france['Cumulative_cases'],label='France')
plt.plot(uk['Date_reported'],uk['Cumulative_cases'],label='The UK')
plt.plot(italy['Date_reported'],italy['Cumulative_cases'],label='Italy')

plt.legend()
plt.show()

greatest_july ='The UK'
lowest_july='France'
increase_march='Italy'