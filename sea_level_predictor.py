import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('C:/Users/PC/Documents/FreeCodeCamp_DataAnalysis_Cert/boilerplate-sea-level-predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit:
    # Get slope and intercept for all data
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create an array of years up to 2050
    years_extended = pd.Series([i for i in range(1880, 2051)])
    
    # Calculate y values: y = mx + c
    line1 = res.slope * years_extended + res.intercept
    
    # Plot the line
    plt.plot(years_extended, line1, 'r')
    

    # Create second line of best fit:
    # Filter data for years >= 2000
    df_recent = df[df['Year'] >= 2000]
    
    # Get new slope and intercept
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create array of years from 2000 to 2050
    years_recent = pd.Series([i for i in range(2000, 2051)])
    
    # Calculate new y values
    line2 = res_recent.slope * years_recent + res_recent.intercept
    
    # Plot the second line
    plt.plot(years_recent, line2, 'green')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title ('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()