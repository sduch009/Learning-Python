#In this Data analysis with Python and Pandas tutorial, we're going to clear some of the Pandas basics.
#Data prior to being loaded into a Pandas Dataframe can take multiple forms, but generally it needs to be a dataset that can form to rows and columns.
#we can turn the below dictionary by importing pands as pd AND by setting dataframe as df = pd.DataFrame(web_stats)
import pandas as pd
import matplotlib.pyplot as plt #SEE LINE 48
from matplotlib import style #SEE LINE 48

style.use('bmh') #SEE LINE 48
#So maybe a dictionary like this:
web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 34, 65, 56, 29, 76],
             'Bounce Rate': [65, 67, 78, 65, 45, 52]}

df = pd.DataFrame(web_stats)
df.set_index('Day', inplace=True) #learned at line 32
#You can call for a quick initial snippit by doing:
print(df.head())
#We can also plot the entire dataframe, so long as the data is normalized on the same scale, this will work fine:
df.plot()
plt.show()
###print(df['Visitors'])
#You can also reference parts of the data frame like an object, so long as there arent any spaces, doing so:
###print(df.Visitors)
#You may also want the last few lines instead.  For this, you can do something like:

###print(df.tail())

#Finally, you can also put the number of the head or tail you want, like so:

###print(df.tail(2))

#You can see here how there are these numbers on the left, 0,1,2,3,4,5 and so on, like line numbers.
#These numbers are actually your "index." The index of a dataframe is what the data is related by, ordered by...etc.
#Generally, it is going to be the variable that connects all of the data.
#In this case, we never defined anything for this purpose, and it would be a challenge for Pandas to just somehow "know" what that variable was.
#Thus, when you do not define an index, Pandas will just make one for you like this.
#Looking at the data set right now, do you see a column that connects the others?

#The "Day" column fits that bill! Generally, if you have any dated data, the date will be the "index" as this is how all of the data points relate.
#There are many ways to identify the index, change the index, and so on.
#We'll cover a couple here. First, on any existing dataframe, we can set a new index like so:
### SEE LINE 11

#Now you can see that those line numbers are gone, and also notice how "Day" is lower than the other column headers, this is done to denote the index.
#One thing to note is the use of inplace=True.  What this does is allow us to modify the datafreame "inplace", whish means we actually modify the variable itself.
#Without inplace=Tur, we would need to do something like:
#### df = df.set_index('Day')

#You can also set multpile indexes, but that's a more advanced topic for maybe a lter date.
#You can do it easily, but reasoning for it is fairly niche.

#Once you have a reasonable index that is either a datetime or a number like we have, then it will work as an X axis.
#If the other columbs are also number data, then you can plot easily:
### SEE LINES 5-8
#Then at the bottom you can plot.
#Remember when we referenced a specific column? Maybe you noticed, but we can reference specific items in a dataframe like this:
###   SEE LINES 18
