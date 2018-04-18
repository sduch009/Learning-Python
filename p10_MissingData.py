import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('bmh')

api_key = '2LWMTZKKbDgy5Zqycxjq'

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states [0] [1] [2:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        #print(abbv)
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.columns = [abbv] ### This is the fix for ValueError:###
        print(query)
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0
        #df = df.pct_change() #For pct change against all df
        #df.rename(columns={'Value':abbv}, inplace=True)
        print(df.head())

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open('fiddy_states3.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df.rename(columns={'Value':'United States'}, inplace=True) #Hotfix, quandl renamed 'United States' as 'Value'
    df["United States"] = (df["United States"] - df["United States"][0]) / df["United States"][0] * 100.0
    return df

#grab_initial_state_data()

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))


HPI_data = pd.read_pickle('fiddy_states3.pickle')
#HPI_State_Correlation = HPI_data.corr()
HPI_data['TX1yr'] = HPI_data['TX'].resample('A', how='mean') #A for annual


print(HPI_data[['TX', 'TX1yr']])
#HPI_data.dropna(inplace=True) #drops any row that has missing data
#HPI_data.dropna(how='all', inplace=True) #only drops rows with all NaN
HPI_data.fillna(method='ffill', inplace=True) #takes data from BEFORE (ffill = forward fill) while backfill takes data from AFTER
print(HPI_data[['TX','TX1yr']].head())


##HPI_data['TX'].plot(ax=ax1, label='Monthly Tx HPI')
##TX1yr.plot(ax=ax1, label='Yearly TX HPI')

HPI_data[['TX','TX1yr']].plot(ax=ax1)

plt.legend(loc=4)
plt.show()
