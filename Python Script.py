# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
data=pd.read_csv('IMDB-Movie-Data.csv')

# %% [markdown]
# 1. Display Top 10 Rows of the Dataset

# %%
data.head(10)

# %% [markdown]
# 2. Check Last 10 Rows of The Dataset

# %%
data.tail(10)

# %% [markdown]
# 3. Find Shape of Our Dataset

# %%
print("Number of Rows:",data.shape[0])
print("Number of Columns:",data.shape[1])

# %% [markdown]
# 4. Getting Information about our Datset
# 

# %%
data.info()

# %% [markdown]
# 5. Checking Null values

# %%
print("Any Missing Value?",data.isnull().values.any())

# %%
data.isnull().sum()

# %%
sns.heatmap(data.isnull())

# %%
## Missing Values in %

per_miss=data.isnull().sum()*100/len(data)
per_miss

# %% [markdown]
# 6. Drop all Missing Values

# %%
data.dropna(axis=0) # Axis=0 : Drop Rows


# %% [markdown]
# 7. Check For Duplicate Data

# %%
duplicate=data.duplicated().any()
print("Are there any duplicate values?",duplicate)

# %%
# If any Duplicate is Present
data=data.drop_duplicates()
data

# %% [markdown]
# 8. Get Overall Statistics About The Dataframe

# %%
# Statistics About Numerical & Categorical Data
data.describe(include='all')

# %% [markdown]
# 9. Display Title of the Movie having Runtime >= 180 Mins

# %%
data.columns

# %%
data[data['Runtime (Minutes)']>=180]['Title']

# %% [markdown]
# 10. In which year there was the Highest Avg Voting ?

# %%
data.columns

# %%
d1=data.groupby('Year')['Votes'].mean().sort_values(ascending=False).index.values

# %%
# Visualisation using Seaborn
# For Ascending/Descending Order use 'Order'
sns.barplot(x='Year',y='Votes',data=data,color='blue',order=d1)
plt.title("Votes By Year")
plt.show()

# %% [markdown]
# 11. In Which Year There was the Highest Avg Revenue?

# %%
data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)

# %%
sns.barplot(x='Year',y='Revenue (Millions)',data=data)
plt.title("Revenue By Year")
plt.show()

# %% [markdown]
# 12. Average Rating for Each Director

# %%
data.groupby('Director')['Rating'].mean().sort_values(ascending=False)

# %% [markdown]
# 13. Display Top 10 Lengthy Movies

# %%
top_10=data.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']]\
.set_index('Title')
top_10

# %%
# Visualisation Using Barplot

sns.barplot(x='Runtime (Minutes)',y=top_10.index,data=top_10,palette='viridis')
plt.show()

# %% [markdown]
# 14. Display Number of Movies Per Year

# %%
data.columns

# %%
data['Year'].value_counts()
sns.countplot(x='Year',data=data)
plt.title('Number of Movies per Year')
plt.show()

# %% [markdown]
# 15. Most Popular Movie Title as per Highest Revenue

# %%
data.columns

# %%
data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]['Title']

# %% [markdown]
# 16. Top 10 Highest Rated Movies and its Directors

# %%
top_10_len=data.nlargest(10,'Rating')[['Title','Rating','Director']].set_index('Title')
top_10_len

# %%
# Visualisation Using Barplot
sns.barplot(x='Rating',y=top_10_len.index,data=top_10_len,hue='Director',dodge=False)
plt.legend(bbox_to_anchor=(1.05,1),loc=2)
plt.show()

# %% [markdown]
# 17. Display Top 10 Highest Revenue Movie Titles

# %%
top10=data.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']].set_index('Title')
sns.barplot(x='Revenue (Millions)',y=top10.index,data=top10,palette='viridis')
plt.title("Top 10 Highest Revenue Movies")
plt.show()

# %% [markdown]
# 18. Avg Rating Yearwise

# %%
data.groupby('Year')['Rating'].mean().sort_values(ascending=False)

# %% [markdown]
# 19. Does Rating affect the Revenue?

# %%
sns.scatterplot(x='Rating',y='Revenue (Millions)',data=data)

# %% [markdown]
# 20. Classify Movies Based on Ratings

# %%
def rating(rating):
    if rating>=7.0:
        return "Excellent"
    elif rating>=6.0:
        return"Good"
    else:
        return"Average"

# %%
data['Rating_cat']=data['Rating'].apply(rating)

# %%
data.tail()

# %% [markdown]
# 21. Count Number of Action Movies

# %%
data['Genre'].dtype

# %%
len(data[data['Genre'].str.contains('Action',case=False)])

# %% [markdown]
# 22. Find Unique Values from Genre Column

# %%
data['Genre']

# %%
list1=[]
for value in data['Genre']:
    list1.append(value.split(','))

# %%
list1

# %%
## Converting into 1-D List
one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)

# %%
one_d

# %%
## Finding Unique Values
unique=[]
for item in one_d:
    if item not in unique:
        unique.append(item)

unique

# %%
# Count of the Unique Genre
len(unique)

# %% [markdown]
# 23. How many Films of Each Genre were made? 

# %%
one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)


# %%
import collections
from collections import Counter
Counter(one_d)

# %%



