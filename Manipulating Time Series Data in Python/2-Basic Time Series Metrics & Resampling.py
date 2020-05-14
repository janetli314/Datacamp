'''
Import 'asset_classes.csv', using .read_csv() to parse dates in the 'DATE' column and set this column as the index, then assign the result to prices.
Select the first price for each series using .iloc[0] on prices and assign the result to first_prices.
Divide prices by first_prices, multiply by 100 and assign the result to normalized.
Plot normalized.
'''
# Import data here
prices = pd.read_csv('asset_classes.csv', parse_dates = ['DATE'], index_col = 'DATE')

# Inspect prices here
print(prices.info())

# Select first prices
first_prices = prices.iloc[0]

# Create normalized
normalized = prices.div(first_prices).mul(100)

# Plot normalized
normalized.plot()
plt.show()

'''
Use pd.read_csv() to import 'nyse.csv' and 'dow_jones.csv', creating a DatetimeIndex for each from the 'date' column using parse_dates and index_col, and assign the result to stocks and dow_jones, respectively.
Use pd.concat() along axis=1 to combine stocks and dow_jones and assign the result to data. Inspect the .info() of data.
Divide data by the first value for each series, multiply by 100 and plot the result.
'''
# Import stock prices and index here
stocks = pd.read_csv('nyse.csv', parse_dates=['date'],index_col = 'date')
dow_jones = pd.read_csv('dow_jones.csv', parse_dates=['date'],index_col = 'date')

# Concatenate data and inspect result here
data = pd.concat([stocks, dow_jones], axis=1)

print(data.info())

# Normalize and plot your data here
Normalize = data.div(data.iloc[0]).mul(100).plot()

plt.show()

'''
Create the list tickers containing the two stock symbols.
Use pd.read_csv() to import 'msft_aapl.csv' and 'sp500.csv', creating a DatetimeIndex for each from the 'date' column using parse_dates and index_col, and assign the result to stocks and sp500, respectively.
Use pd.concat() to concatenate stocks and sp500 along axis=1, apply .dropna() to drop all missing values, and assign the result to data.
Normalize data by dividing by the first price, multiply by 100 and assign the output to normalized.
Select tickers from normalized, and subtract normalized['SP500'] with keyword axis=0 to align the indexes, then plot the result.
'''
# Create tickers
tickers = ['MSFT','AAPL']

# Import stock data here
stocks = pd.read_csv('msft_aapl.csv', parse_dates=['date'],index_col='date')

# Import index here
sp500 = pd.read_csv('sp500.csv', parse_dates=['date'],index_col='date')

# Concatenate stocks and index here
data = pd.concat([stocks,sp500],axis=1).dropna()

# Normalize data
normalized = data.div(data.iloc[0]).mul(100)

# Subtract the normalized index from the normalized stock prices, and plot the result
diff = normalized[tickers].sub(normalized['SP500'],axis=0).plot()

plt.show()

'''
Create monthly_dates using pd.date_range with start, end and frequency alias 'M'.
Create and print the pd.Series monthly, passing the list [1, 2] as the data argument, and using monthly_dates as index.
Create weekly_dates using pd.date_range with start, end and frequency alias 'W'.
Apply .reindex() to monthly three times: first without additional options, then with bfill and then with ffill, print()-ing each result.
'''
# Set start and end dates
start = '2016-1-1'
end = '2016-2-29'

# Create monthly_dates here
monthly_dates = pd.date_range(start = start , end = end, freq = 'M')

# Create and print monthly here
monthly = pd.Series(data = [1,2], index= monthly_dates)
print(monthly)

# Create weekly_dates here
weekly_dates = pd.date_range(start = start,end = end, freq='W')

# Print monthly, reindexed using weekly_dates
print(monthly.reindex(weekly_dates))
print(monthly.reindex(weekly_dates,method = 'bfill'))
print(monthly.reindex(weekly_dates,method = 'ffill'))

'''
Use pd.read_csv() to import 'unemployment.csv', creating a DateTimeIndex from the 'date' column using parse_dates and index_col, and assign the result to data.
Convert data to weekly frequency using .asfreq() with the alias 'W' and show the first five rows.
Convert again to weekly frequency, adding the option 'bfill' and show the first five rows.
Create weekly series, now adding the option 'ffill', assign to weekly_ffill and show the first five rows.
Plot weekly_ffill starting in 2015.
'''
# Import data here
data = pd.read_csv('unemployment.csv',parse_dates = ['date'],index_col = 'date')

# Show first five rows of weekly series
print(data.asfreq('W').head())

# Show first five rowsjavascript:void(0) of weekly series with bfill option
print(data.asfreq('W', method = 'bfill').head())

# Create weekly series with ffill option and show first five rows
weekly_ffill = data.asfreq('W', method = 'ffill')
print(weekly_ffill.head())

# Plot weekly_fill starting 2015 here 
weekly_ffill.loc['2015': ].plot()

plt.show()

'''
Inspect monthly using .info().
Create a pd.date_range() with weekly dates, using the .min() and .max() of the index of monthly as start and end, respectively, and assign the result to weekly_dates.
Apply .reindex() using weekly_dates to monthly and assign the output to weekly.
Create new columns 'ffill' and 'interpolated' by applying .ffill() and .interpolate() to weekly.UNRATE.
Show a plot of weekly.
'''
# Inspect data here
print(monthly.info())

# Create weekly dates
weekly_dates = pd.date_range(monthly.index.min(),end=monthly.index.max(),freq = 'W')

# Reindex monthly to weekly data
weekly = monthly.reindex(weekly_dates)

# Create ffill and interpolated columns
weekly['ffill'] = weekly.UNRATE.ffill()
weekly['interpolated'] = weekly.UNRATE.interpolate()

# Plot weekly
weekly.plot()
plt.show()

'''
Use pd.read_csv() to import 'debt_unemployment.csv', creating a DateTimeIndex from the 'date' column using parse_dates and index_col, and assign the result to data. print() the .info() of the data.
Apply .interpolate() to data and assign this to interpolated, then inspect the result.
Plot interpolated with 'Unemployment' on the secondary_y axis.
'''
# Import & inspect data here
data = pd.read_csv('debt_unemployment.csv', parse_dates=['date'], index_col='date')
print(data.info())

# Interpolate and inspect here
interpolated = data.interpolate()
print(interpolated.info())

# Plot interpolated data here
interpolated.plot(secondary_y= 'Unemployment')
plt.show()

'''
Use pd.read_csv() to import 'ozone.csv' and set a DateTimeIndex based on the 'date' column using parse_dates and index_col, assign the result to ozone and inspect using .info().
Apply .resample() with weekly frequency ('W') to ozone, aggregate using .mean() and plot the result.
Repeat with monthly ('M') and annual ('A') frequencies, plotting each result.
'''
# Import and inspect data here
ozone = pd.read_csv('ozone.csv', parse_dates= ['date'], index_col='date')
print(ozone.info())


# Calculate and plot the weekly average ozone trend
ozone.resample('W').mean().plot()
plt.show()


# Calculate and plot the monthly average ozone trend
ozone.resample('M').mean().plot()
plt.show()

# Calculate and plot the annual average ozone trend
ozone.resample('A').mean().plot()
plt.show()

'''
Use pd.read_csv() to import 'stocks.csv' and set a DateTimeIndex based on the 'date' column using parse_dates and index_col, assign the result to stocks and inspect using .info().
Create monthly_average by applying .resample() with monthly frequency to data, using .mean() to aggregate. Plot the result using subplots.
'''
# Import and inspect data here
stocks = pd.read_csv('stocks.csv', parse_dates= ['date'], index_col='date')
print(stocks.info())

# Calculate and plot the monthly averages
monthly_average = stocks.resample('M').mean()
monthly_average.plot(subplots = True)
plt.show()

'''
Use pd.read_csv() to import 'gdp_growth.csv' and 'djia.csv', for both set a DateTimeIndex based on the 'date' column using parse_dates and index_col, and assign the results to gdp_growth and djia respectively, then inspect using .info().
Resample djia using frequency alias 'QS', aggregate using .first(), and assign to djia_quarterly.
Apply .pct_change() to djia_quarterly and .mul() by 100 to obtain djia_quarterly_return.
Use pd.concat() to concatenate gdp_growth and djia_quarterly_return along axis=1, and assign to data. Rename the columns using .columns and the new labels 'gdp' and 'djia', then .plot() the results.
'''
# Import and inspect gdp_growth here
gdp_growth = pd.read_csv('gdp_growth.csv', parse_dates=['date'], index_col='date')
print(gdp_growth.info())

# Import and inspect djia here
djia = pd.read_csv('djia.csv', parse_dates=['date'], index_col='date')
print(djia.info())


# Calculate djia quarterly returns here 
djia_quarterly = djia.resample('QS').first()
djia_quarterly_return = djia_quarterly.pct_change().mul(100)

# Concatenate, rename and plot djia_quarterly_return and gdp_growth here 
data = pd.concat([gdp_growth, djia_quarterly_return], axis=1)

data.columns = ['gdp', 'djia']

data.plot()
plt.show()

'''
Use pd.read_csv() to import 'sp500.csv', set a DateTimeIndex based on the 'date' column using parse_dates and index_col, assign the results to sp500, and inspect using .info().
Convert sp500 to a pd.Series() using .squeeze(), and apply .pct_change() to calculate daily_returns.
.resample() daily_returns to month-end frequency (alias: 'M'), and apply .agg() to calculate 'mean', 'median', and 'std'. Assign the result to stats.
.plot() stats
'''
# Import data here
sp500 = pd.read_csv('sp500.csv', parse_dates=['date'], index_col='date')
 
# Calculate daily returns here
daily_returns = sp500.squeeze().pct_change()
 
# Resample and calculate statistics
stats = daily_returns.resample('M').agg(['mean', 'median', 'std'])
 
# Plot stats here
stats.plot()
plt.show()



