from itertools import count
from pandas.core.internals.managers import make_na_array
from pytz import country_names

from time import process_time

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Step 1: Define the file paths
sanjoaquin_path = r'C:\Users\kevin\PycharmProjects\HackMerced2025\SanJoaquinData.txt'
alameda_path = r'C:\Users\kevin\PycharmProjects\HackMerced2025\AlamedaCountyData.txt'
oc_path = r'C:\Users\kevin\PycharmProjects\HackMerced2025\OCData.txt'
file_paths = [sanjoaquin_path, alameda_path, oc_path]
county_names = ['San Joaquin', 'Alameda', 'OC']
# Step 2: Process the data
def process_and_plot(file_paths, county_names):
    earned = 0
    for file_path, county_name in zip(file_paths, county_names):
        data = pd.read_csv(file_path)
        data['Income'] = data['Income'].replace('[\$,]', '', regex=True).astype(float)
        data.set_index('Year', inplace=True)
        data.reset_index(inplace=True)
        X = data['Year'].values
        y = data['Income'].values
        X_mean = np.mean(X)
        y_mean = np.mean(y)
        slope = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean) ** 2)
        b0 = y_mean - slope * X_mean
        future_years = np.arange(2023, 2100)
        predictions = b0 + slope * future_years
        earned = np.cumsum(predictions)
        print(earned)
        # plt.figure(figsize=(12, 6))
        # plt.plot(data['Year'], data['Income'], marker='o', label='Actual Income')
        # plt.plot(future_years, predictions, marker='x', linestyle='--', color='red', label='Predicted Income')
        # plt.title(f'Per Capita Personal Income in {county_name} County (1970-2030)')
        # plt.xlabel('Year')
        # plt.ylabel('Income ($)')
        # plt.legend()
        # plt.grid(True)
        # plt.show()

process_and_plot(file_paths,county_names)


