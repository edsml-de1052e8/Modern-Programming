# Lecture 6: Working with Data in Pandas
### 19/10/21

Pandas is for table datasets, used a lot in machine learning for data frames. Loads of manipulation and operations available.

```import pandas as pd```

2 Basic objects available in pandas:
- Dataframe: a table with array of individual entries each with a specific value. Each entry corresponds to a row and a column. Think about dataframes as sets of series.
eg. pd.DataFrame({'Bob'['I liked it']}
- Series: sequence of data values, series. eg. ``` pd.Series([1, 2, 3, 4])


*Reading data file*

- Usually from CSV file. using ```pd.read_csv("filename.csv")```

Other commmands
```dataframe.shape```
```dataframe.head``` : to get it to print first few rows
```index_column=0```: adds an index as the first column with 0, 1, 2, 3 per row.


- When a table is created then you can access each column and row with a specific index
Df['country'] : accesses column country from a DataFrame

**Indexing Operators**

- Index-based selection: selects DF based on numerical position in data using ```iloc``` parameter
eg. DF.iloc[0] : accesses first row of data
NB: iloc[0] grabs ROWS first vs index accesses COLUMNS first 


iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

The : operator comes from native Python and means 'everything'. So can be used to indicate range of values.
eg. ```DF.iloc[:3,0]``` so prints everything before 3, all ROWS before 3 with first column

- Negative numbers can also be used in selection

- Label-based selection: 2nd paradigm for attribute selection. Using the ```loc``` operator. Here the data index value matters not the position.
eg. reviews.loc[0, 'country']

This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them! To get 1000 elements using loc, you will need to go one lower and ask for df.loc[0:999].


**Manipulating the index***

Label-based selection derives its power from the labels in the index. Critically, the index we use is not immutable. We can manipulate the index in any way we see fit.

The ```set_index()``` method can be used to do the job. Here is what happens when we set_index to the title field:

```DF.set_index("title")```

- Can use Ampersand to combine criterias.
```reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]```
this selects all wines from Italy that have review points over and equal to 90

This can also be changed to: ```reviews.loc[(reviews.country == 'Italy or France') & (reviews.points >= 90)]``` 
the 'or' statement will combine values from both variables appplied to the criteria of above or equal to 90 points.

- Null values: The second is isnull (and its companion notnull). These methods let you highlight values which are (or are not) empty (NaN).

**Assigning data**
- Assigning data to dataframe using constant value: eg. ```DataFrame['header'] = 'everyone' ``` changes whatever the entry is to all rows with everyone value.

```reviews['critic'] = 'everyone' reviews['critic'] ```

**Summary Functions**

However, the data does not always come out of memory in the format we want it in right out of the bat. Sometimes we have to do some more work ourselves to reformat it for the task at hand. This tutorial will cover different operations we can apply to our data to get the input just right.

- ```describe()``` method: gives summary of data present in that column. Only makes sense for numerical data.
```dataFrame.column.describe()```

- To get the mean of an attribute: ```.mean``` function can be used. 
```dataFrame.columnname.mean()```

- For a list of unique values such as strings: ```.unique``` function can be used.

-```value.counts()```: to see a list of unique values of a particular string, use the value.counts function.


**Maps**

- Maps: A map is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values. 
In data science we often have a need for creating new representations from existing data, or for transforming data from the format it is in now to the format that we want it to be in later.

map() is the first, and slightly simpler one. For example, suppose that we wanted to remean the scores the wines received to 0. We can do this as follows:

```review_points_mean = reviews.points.mean()reviews.points.map(lambda p: p - review_points_mean)```

The function you pass to map() should expect a single value from the Series (a point value, in the above example), and return a transformed version of that value. map() returns a new Series where all the values have been transformed by your function.

```apply()``` is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.

Both map and apply don't modifiy the original values. Can also do *operations* on these values: 

Remean:
```review_points_mean = reviews.points.mean()  reviews.points - review_points_mean```

Combining columns:

```reviews.country + " - " + reviews.region_1``` : here the - sign combines the country to the region with added "-" in the middle of the string and will add it to every data entry.

- These operations are fastr than map or apply because they uitlize in-built pandas speed ups (C code under the hood).

**Grouping**

Maps allow us to transform data in a DataFrame or Series one value at a time for an entire column. However, often we want to group our data, and then do something specific to the group the data is in.

As you'll learn, we do this with the groupby() operation. We'll also cover some additional topics, such as more complex ways to index your DataFrames, along with how to sort your data.

groupby() created a group of reviews which allotted the same point values to the given wines. Then, for each of these groups, we grabbed the points() column and counted how many times it appeared. value_counts() is just a shortcut to this groupby() operation.

We can use any of the summary functions we've used before with this data. For example, to get the cheapest wine in each point value category, we can do the following:

```reviews.groupby('points').price.min()```

You can think of each group we generate as being a slice of our DataFrame containing only data with values that match. This DataFrame is accessible to us directly using the apply() method, and we can then manipulate the data in any way we see fit. For example, here's one way of selecting the name of the first wine reviewed from each winery in the dataset:

```reviews.groupby('winery').apply(lambda df: df.title.iloc[0])```

Out[67]:
winery
1+1=3                          1+1=3 NV Rosé Sparkling (Cava)
10 Knots                 10 Knots 2010 Viognier (Paso Robles)


For even more fine-grained control, you can also group by more than one column. For an example, here's how we would pick out the best wine by country and province:

```reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])```

- ```agg``` function: aggregate, to run multiple functions together on the DF.

```reviews.groupby(['country']).price.agg([len, min, max])```

**Multi-Indices**

A multi-index differs from a regular index in that it has multiple levels. Creates a sense of dependency of how data is displayed with each other.

For example:
```countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len]).        countries_reviewed```

then retable it:

```mi = countries_reviewed.index. type(mi)```


**Sorting**
Looking again at countries_reviewed we can see that grouping returns data in 'index' order, not in value order. That is to say, when outputting the result of a groupby, outside of the initial grouping the order of the rows is dependent on the values in the index, not in the data.

To get data in the order want it in we can sort it ourselves. The ```sort_values()``` method is handy for this.

```countries_reviewed = countries_reviewed.reset_index().   countries_reviewed.sort_values(by='len')```

This sorts column by length of data, automatically from lowest to highest.

- Can also change the sorting from either high to low or low to high.
```countries_reviewed.sort_values(by='len', ascending=False)```  with ascending=False argument makes the highest number first and goes to the lowest.

- Can also sort with multiple values 
```countries_reviewed.sort_values(by=['country', 'len'])```. Here this will sort in ascending order (from A-Z) the lsit of countries with reviews and the length (the number of reviews) in ascending order.
Note that here this makes the arguments country and len dependent on each other so that the first values that will appear are the lowest ones with both low len and country values.

**Data Types & Missing Values**

- Dtypes: data type for a column in a DF or series.

You can use the dtype property to grab the type of a specific column. For instance, we can get the dtype of the price column in the reviews DataFrame and it will return things such as float64:
```reviews.price.dtype```


Data types tell us something about how pandas is storing the data internally. float64 means that it's using a 64-bit floating point number; int64 means a similarly sized integer instead, and so on.

One peculiarity to keep in mind (and on display very clearly here) is that columns consisting entirely of strings do not get their own type; they are instead given the object type.

It's possible to convert a column of one type into another wherever such a conversion makes sense by using the ```astype()``` function. For example, we may transform the points column from its existing int64 data type into a float64 data type:

```reviews.points.astype('float64')```

An entire DataFrame or Series has its own dtype too.

**Missing Data**

Entries missing values are given the value NaN, short for "Not a Number". For technical reasons these NaN values are always of the float64 dtype.

Pandas provides some methods specific to missing data. To select NaN entries you can use pd.isnull() (or its companion pd.notnull()). This is meant to be used thusly: ```reviews[pd.isnull(reviews.country)]``` grabs all entries where the country column is not a number (NaN).

To amend that you can assign NaN to a specific value or string using the ```fillna()``` function
eg. ```reviews.region_2.fillna("Unknown")```

- ```backfill()``` function:  fill each missing value with the first non-null value that appears sometime after the given record in the database.
- ```.replace()``` function: to replace one value and assign all entries to this new value.
eg. ```reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")```. Here all values called @kerinokeefe were changed to @kerino.

**Renaming**

- ```.rename()``` function: lets you change index names and/or column names. For example, to change the points column in our dataset to score, we would do:

```reviews.rename(columns={'points': 'score'})``` . This passes a dictioanry with value yo uwant to assign and what you want to replace it with.

rename() lets you rename index or column values by specifying a index or column keyword parameter, respectively. It supports a variety of input formats, but usually a Python dictionary is the most convenient. Here is an example using it to rename some elements of the index.

```reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})``` 

- To rename indices specifically: use the ```set_index()``` function or ```rename_axis()```

Both the row index and the column index can have their own name attribute. The complimentary rename_axis() method may be used to change these names. For example:

```reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')```

**Combining**

Pandas has three core methods for doing this. In order of increasing complexity, these are ```concat()```, ```join()```, and ```merge()```. Most of what merge() can do can also be done more simply with join(), so we will omit it and focus on the first two functions here.

- The simplest combining method is concat(). Given a list of elements, this function will combine those elements together along an axis.

This is useful when we have data in different DataFrame's or Series objects but having the same fields (columns).


```s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])

pd.concat([s1, s2])```

- ```pd.join()```

- And if we want to re-index we just use the ```.reset_index()``` method again:

```# See https://pandas.pydata.org/docs/user_guide/merging.html for further details
left = pd.DataFrame(
    {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
)

right = pd.DataFrame(
    {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}, index=["K0", "K2", "K3"]
)
result = left.join(right)
result```

- Join can be specified in the manner: To modify the way dataframes are joined, one of the arguments we have available to us is the 'how' argument:

```result = left.join(right, how="outer")
result```

Notice the use of ```how="outer"``` to specify joining manner. Other options are available too:

Whilst what giving the 'how' argument as "outer" and "inner" is achieving is clear from the above, the naming convention and what other options are available are now. To understand better we can take a look at the 'how' section of the join methods docstring:

how{‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘left’

    How to handle the operation of the two objects.

        left: use calling frame’s index (or column if on is specified)

        right: use other’s index.

        outer: form union of calling frame’s index (or column if on is specified) with other’s index, and sort it. lexicographically.

        inner: form intersection of calling frame’s index (or column if on is specified) with other’s index, preserving the order of the calling’s one.






































