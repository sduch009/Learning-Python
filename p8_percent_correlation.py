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
        print(main_df.head())


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

##fig = plt.figure()
##ax1 = plt.subplot2grid((1,1), (0,0))

#HPI_data = pd.read_pickle('fiddy_states.pickle') #for pct change against entire dataframe
HPI_data = pd.read_pickle('fiddy_states3.pickle')

##benchmark = HPI_Benchmark()

##HPI_data.plot(ax = ax1)
##benchmark.plot(ax=ax1, color='k', linewidth=10)

##plt.legend().remove()
##plt.show()

HPI_State_Correlation = HPI_data.corr() #Shows the level of correlation with EACH other variable
print(HPI_State_Correlation)

#HPI_State_Correlation.describe()
print(HPI_State_Correlation.describe()) #Describes dataframe : Count, mean, stf, min Quartiless, max
