# IO = Input/Output

#Welcome to Part 3 of Data Analysis with Pandas and Python. In this tutorial, we will begin discussing IO, or input/output, with Pandas, and begin with a realistic use-case.
#To get ample practice, a very useful website is Quandl. Quandl contains a plethora of free and paid data sources.
#What makes this location great is that the data is generally normalized, it's all in one place, and extracting the data is the same method.
#If you are using Python, and you access the Quandl data via their simple module, then the data is automatically returned to a dataframe.
#For the purposes of this tutorial, we're going to just manually download a CSV file instead, for learning purposes, since not every data source you find is going to have a nice and neat module for extracting the datasets.

#Let's say we're interested in maybe purchasing or selling a home in Austin, Texas. The zipcode there is 77006.
#We could go to the local housing listings and see what the current prices are, but this doesn't really give us any real historical information, so let's just try to get some data on this.
#Let's query for "home value index 77006." Sure enough, we can see an index here. There's top, middle, lower tier, three bedroom, and so on. Let's say, sure, we got a a three bedroom house. Let's check that out.
#Turns out Quandl already provides graphs, but let's grab the dataset anyway, make our own graph, and maybe do some other analysis.
#Go to download, and choose CSV. Pandas is capable of IO with csv, excel data, hdf, sql, json, msgpack, html, gbq, stata, clipboard, and pickle data, and the list continues to grow.
#Check out the IO Tools documentation for the current list. Take that CSV and move it into the local directory (the directory that you are currently working in / where this .py script is).
#Starting with this code, loading in a CSV to a dataframe can be as simple as:
import pandas as pd

df = pd.read_csv('p3_quandldata.csv')
#setting our index column as the Date values
df.set_index('Date', inplace = True)
#setting the "values" as House prices doing:
df.columns = ['House Prices']
#and printing
print(df.head())
#Notice that we have no decent index again. We can fix that like we did before doing:
#now, Lets say we want to send this back to a CSV, we can do:
###df.to_csv('newcsv2.csv')
#We only ahve the one column right now, but if you had many colums, and just wanted to send one, you could do

###df['Value'].to_csv('newcsv2.csv')
#Now let's read that new CSV in:

###df = pd.read_csv('newcsv2.csv')
###print(df.head())

#index is gone again, because csv has no index attribute like our df does.  we can set the index on import rather than importing and then setting the index, something like:

###df = pd.read_csv('newcsv2.csv', index_col=0)
###print(df.head())
#Exporting to html like so:
df.to_html('example.html')
