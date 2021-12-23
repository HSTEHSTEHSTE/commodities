import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def percentage_of_greater_def(sequence, min_price_dif=5):
    dif = np.array(sequence['Price_dif'])
    number_of_greater = np.where(dif >= min_price_dif)[0].size
    total_number = len(sequence)
    print(number_of_greater / total_number)


def plot_against_single_line(sequence, line_height):
    date_sequence = np.array(sequence['Date']).astype('datetime64')
    line = np.full(date_sequence.size, line_height)

    plt.plot(date_sequence, sequence['Price_dif'])
    plt.plot(date_sequence, line)
    plt.show()


brent_day_file = 'C:\\Users\\HSTE\\oil-prices\\data\\brent-daily.csv'
wti_day_file = 'C:\\Users\\HSTE\\oil-prices\\data\\wti-daily.csv'
brent_month_file = 'C:\\Users\\HSTE\\oil-prices\\data\\brent-monthly.csv'
wti_month_file = 'C:\\Users\\HSTE\\oil-prices\\data\\wti-monthly.csv'
brent_year_file = 'C:\\Users\\HSTE\\oil-prices\\data\\brent-year.csv'
wti_year_file = 'C:\\Users\\HSTE\\oil-prices\\data\\wti-year.csv'

brent_day = pd.read_csv(brent_day_file)
wti_day = pd.read_csv(wti_day_file)
brent_month = pd.read_csv(brent_month_file)
wti_month = pd.read_csv(wti_month_file)
brent_year = pd.read_csv(brent_year_file)
wti_year = pd.read_csv(wti_year_file)

day = pd.merge(brent_day, wti_day, on=['Date'])
day['Price_dif'] = day['Price_x'] - day['Price_y']
day['Price_dif_ratio'] = day['Price_dif']/day['Price_x']

month = pd.merge(brent_month, wti_month, on=['Date'])
month['Price_dif'] = month['Price_x'] - month['Price_y']
month['Price_dif_ratio'] = month['Price_dif']/month['Price_x']

year = pd.merge(brent_year, wti_year, on=['Date'])
year['Price_dif'] = year['Price_x'] - year['Price_y']
year['Price_dif_ratio'] = year['Price_dif']/year['Price_x']

# plot_against_single_line(month, 5)

percentage_of_greater_def(day)
