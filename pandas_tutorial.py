#In this Data analysis with Python and Pandas tutorial, we're going to clear some of the Pandas basics.
#Data prior to being loaded into a Pandas Dataframe can take multiple forms, but generally it needs to be a dataset that can form to rows and columns.
#we can turn the below dictionary by importing pands as pd AND by setting dataframe as df = pd.DataFrame(web_stats)
import pandas as pd
#So maybe a dictionary like this:
web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 34, 65, 56, 29, 76],
             'Bounce Rate': [65, 67, 78, 65, 45, 52]}

df = pd.DataFrame(web_stats)
#You can call for a quick initial snippit by doing:
print(df.head())

#You may also want the last few lines instead.  For this, you can do something like:
print(df.tail())
#Finally, you can also put the number of the head or tail you want, like so:
print(df.tail(2))
