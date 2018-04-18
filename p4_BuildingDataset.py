import quandl
import pandas as pd
api_key = '2LWMTZKKbDgy5Zqycxjq'

#df = quandl.get('FMAC/HPI_AK', authtoken=api_key, start_date="1999-01-31")

#print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#This is a list:
#print(fiddy_states)

#This is a dataframe:
#print(fiddy_states[0])

#This is a column:
print(fiddy_states[0][1])

for abbv in fiddy_states [0] [1] [2:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))
