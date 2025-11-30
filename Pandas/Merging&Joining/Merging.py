import pandas as pd

# customer dataframe
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Ramesh', 'Suresh', 'Kalpesh']
})

# order dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderAmount': [250, 450, 350]
})

df=pd.merge(df_customers,df_orders,on="CustomerID",how="inner")
print(df)