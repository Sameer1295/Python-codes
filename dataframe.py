import pandas as pd

data = {
    "batsman":['rohit','kl','kohli'],
    "scores":[12,23,50]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
print(df.loc[2]) #locate row
print(df.loc[[0,1]]) #return a series
