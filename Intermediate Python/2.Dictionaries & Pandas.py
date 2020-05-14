'''
Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
Use ind_ger to access the capital of Germany from the capitals list. Print it out.
'''
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index("germany")    #index = 2

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

'''
With the strings in countries and capitals, create a dictionary called europe with 4 key:value pairs. Beware of capitalization! Make sure you use lowercase characters everywhere.
Print out europe to see if the result is what you expected.
'''
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid', "france":"paris","germany":'berlin','norway':'oslo'}

# Print europe
print(europe)
'''
Check out which keys are in europe by calling the keys() method on europe. Print out the result.
Print out the value that belongs to the key 'norway'.
'''
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe["norway"])
'''
Add the key 'italy' with the value 'rome' to europe.
To assert that 'italy' is now a key in europe, print out 'italy' in europe.
Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
Print out europe.
'''
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)
'''
The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
Australia is not in Europe, Austria is! Remove the key 'australia' from europe.
Print out europe to see if your cleaning work paid off.
'''
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)



