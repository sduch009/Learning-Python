import pandas as pd
#For similar data, merge when index does not matter, join when index matters, concatenate for elongating/adding to, appending for adding to the end
#https://pythonprogramming.net/join-merge-data-analysis-python-pandas-tutorial/?completed=/concatenate-append-data-analysis-python-pandas-tutorial/
df1 = pd.DataFrame({#'HPI':[80,85,88,85],
                    'Year': [2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]})#,
                  # index = [2001, 2002, 2003, 2004])

#df2 = pd.DataFrame({'HPI':[80,85,88,85],
                #    'Int_rate':[2, 3, 2, 2],
                #    'US_GDP_Thousands':[50, 55, 65, 55]},
                 #  index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({#'HPI':[80,85,88,85],
                    'Year':[2001, 2003, 2004, 2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]})#,
                  # index = [2001, 2002, 2003, 2004])
#The only major change is in df3 ,where we change int_rate to unemployment. First, let's discuss merging.

#print(pd.merge(df1, df2, on = ['HPI' , 'Int_rate']))

#Now we are going to join df1 and df3.

#df1.set_index('HPI', inplace=True)
#df3.set_index('HPI', inplace=True)
#Now they share an index but no columns so we do:
#joined = df1.join(df3)
#print(joined) #That brings data replication, so not ideal


merged = pd.merge(df1, df3, on = 'Year', how = 'left') #how can be = 'right' , 'outer', or 'inner' also...
merged.set_index('Year', inplace = True)
print(merged)
