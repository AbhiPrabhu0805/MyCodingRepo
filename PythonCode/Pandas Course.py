#### Pandas Course

import pandas as pd

data =[["John",40,"AVP"],["Abhimanyu",32,"Contractor"],["Rohit",35,"Director"],["TBD",None,"Vacant"]]

cols=["Name","Age","Position"]

df=pd.DataFrame(data=data, columns=cols)

print(df)

print(df["Age"])

print(df.dtypes)

print(df["Age"]*2)
print(df["Age"]*3-1)

print(df["Age"][0])


print(df[["Name","Age"]][:1])
print(len(df["Age"]))
print(len(df["Position"]))



## advanced Pandas

df2= pd.read_csv('business-financial-data-september-2023-quarter.csv')

print(df2.head(10))

print(df2.tail(10))

print(df2["Period"].head(10))  ##get limited rows for specifiv column

df2=df2.rename(columns={"Period": "Prd"}) #Rename column name

print(df2.head(10))
 
filtered_df2=df2[df2["STATUS"]!='F']  #filter using data frames. Need to use boolen array inside the df[] as it has value of True or False for every row

print(filtered_df2.head(100))


#### Pandas boolean operators:
## AND -> &
## OR -> |
## NOT -> ~

multi_fil_df2=df2[(df2["STATUS"]!='F') & (df2["Suppressed"]!='NaN')] ## Using & operator. Parenthesis is required! for each boolean array

print(multi_fil_df2.head(10))


### Aggregate functions

print(df2["Data_value"].mean())
print(df2["Data_value"].min())
print(df2["Data_value"].max())
print(df2["Data_value"].describe())
print(df2[["Prd","Data_value","STATUS"]].describe())

print(df2.groupby(["Series_reference"])[["Data_value"]].mean().head(10))
grouped_df=df2.groupby(["Series_reference"])[["Data_value"]].mean().round(2).head(10)
print(grouped_df)
print(grouped_df.columns)
reset_index_df=grouped_df.reset_index()
print(reset_index_df.columns)
print(reset_index_df)


print(df2.sort_values(["Data_value"]).head(10))# by default it will sort in ascending
print(df2["Data_value"].sort_values().head(10))

print(df2.sort_values(["Data_value"], ascending=False).head(10)) # to sort in descending

## checking for missing values / NaN

nandf=df2[["Series_reference","Data_value","Suppressed"]]

print(nandf)

print(nandf.isna().sum())
print(nandf.count())
print(len(nandf))
print(len(df2))
print(len(df))

print(nandf.dropna())
print(nandf.fillna("Missing"))

print(nandf.fillna({"Suppressed":"Missing","Data_value":0.000}))

nandf.to_csv("df_output.csv")




