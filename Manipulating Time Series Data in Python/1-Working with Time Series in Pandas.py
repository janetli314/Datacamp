'''
We have already imported pandas as pd for you.

Use pd.date_range to create seven dates starting from '2017-1-1' at (default) daily frequency. Use the arguments start and periods. Assign the result to seven_days.
Iterate over each date in seven_days and in each iteration, print the .dayofweek and .weekday_name attributes.
'''

# Create the range of dates here
seven_days = pd.date_range(start = '2017-1-1', periods = 7, freq = 'D')

# Iterate over the dates and print the number and name of the weekday
for day in seven_days:
    print(day.dayofweek, day.weekday_name)

'''
We have already imported pandas as pd and matplotlib.pyplot as plt for you, and loaded the air quality DataFrame into the variable data.

Inspect data using .info().
Use pd.to_datetime to convert the column 'date' to dtype datetime64.
Set the 'date' column as index.
Validate the changes by inspecting data using .info() again.
Plot data using subplots=True.
'''
data = pd.read_csv('nyc.csv')

# Inspect data
print(data.info())

# Convert the date column to datetime64
data.date = pd.to_datetime(data.date)

# Set date column as index
data.set_index('date', inplace = True)

# Inspect data 
print(data.info())

# Plot data
data.plot(subplots = True)
plt.show()

'''
Create an empty pd.DataFrame() called prices.
Iterate over a list containing the three years, 2013, 2014, and 2015, as string, and in each loop:
Use the iteration variable to select the data for this year and the column price.
Use .reset_index() with drop=True to remove the DatetimeIndex.
Rename the column price column to the appropriate year.
Use pd.concat() to combine the yearly data with the data in prices along axis=1.
Plot prices
'''
# Create dataframe prices here
prices = pd.DataFrame()
 
# Select data for each year and concatenate with prices here 
for year in ['2013', '2014', '2015']:
    price_per_year = yahoo.loc[year, ['price']].reset_index(drop=True)   #price_per_year DataFrame
    #price_per_year.rename(columns={'price': year}, inplace=True)
    price_per_year = price_per_year.rename(columns = {'price': year})
    prices = pd.concat([prices, price_per_year], axis=1)
    
 
# Plot prices
prices.plot()
plt.show()

'''
Inspect co using .info().
Use .asfreq() to set the frequency to calendar daily.
Show a plot of 'co' using subplots=True.
Change the the frequency to monthly using the alias 'M'.
Show another plot of co using subplots=True
'''
# Inspect data
print(co.info())

# Set the frequency to calendar daily
co = co.asfreq('D')

# Plot the data
co.plot(subplots = True)
plt.show()

# Set frequency to monthly
co = co.asfreq('M')

# Plot the data
co.plot(subplots = True)
plt.show()

'''
Use pd.read_csv() to import 'google.csv', parsing the 'Date' as dates, setting the result as index and assigning to google.
Use .asfreq() to set the frequency of google to business daily.
Add new columns lagged and shifted to google that contain the Close shifted by 90 business days into past and future, respectively.
Plot the three columns of google.
'''
# Import data here
google = pd.read_csv('google.csv',parse_dates=['Date'],index_col='Date')

# Set data frequency to business daily
google = google.asfreq('B')

# Create 'lagged' and 'shifted'
google['lagged'] = google.Close.shift(-90)
google['shifted'] = google.Close.shift(90)

# Plot the google price series
google.plot()
plt.show()

'''
Create a new column called shifted_30 that contains the 'price' shifted by 30 business days into the future.
Subtract 'shifted_30' from 'price', and assign the result to a new column, 'change_30'.
Apply .diff(), setting periods to 30, and assign the result to a new column, 'diff_30'.
Inspect the last five rows of yahoo to verify the calculation.
Subtract diff_30 from change_30 using the .sub() method and print the .value_counts() of the result to show both columns are equal.
'''
# Created shifted_30 here
yahoo['shifted_30'] = yahoo.price.shift(30)

# Subtract shifted_30 from price
#yahoo['change_30'] = yahoo['price'] - yahoo['shifted_30']
yahoo['change_30'] = yahoo.price.sub(yahoo.shifted_30)

# Get the 30-day price difference
yahoo['diff_30'] = yahoo.price.diff(30)

# Inspect the last five rows of price
print(yahoo.tail())

# Show the value_counts of the difference between change_30 and diff_30
print(yahoo.change_30.sub(yahoo.diff_30).value_counts())


'''
We have already imported pandas as pd, and matplotlib.pyplot as plt. We have also loaded 'GOOG' stock prices for the years 2014-2016, set the frequency to calendar daily, and assigned the result to google.

Create the columns 'daily_return', 'monthly_return', and 'annual_return' that contain the pct_change() of 'Close' for 1, 30 and 360 calendar days, respectively, and multiply each by 100.
Plot the result using subplots=True.
'''
# Create daily_return
google['daily_return'] = google.Close.pct_change(1).mul(100)

# Create monthly_return
google['monthly_return'] = google.Close.pct_change(30).mul(100)

# Create annual_return
google['annual_return'] = google.Close.pct_change(360).mul(100)

# Plot the result
google.plot(subplots = True)
plt.show()

'''

