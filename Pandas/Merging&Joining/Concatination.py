import pandas as pd

# region1
df_Region1 = pd.DataFrame({
    'CustomerID': [1, 2],
    'Name': ['Gopal', 'Raju']
})

# region2
df_Region2 = pd.DataFrame({
    'CustomerID': [3, 4],
    'Name': ['Shyam', 'Baburao']
})
concaniate=pd.concat([df_Region1,df_Region2],axis=1,ignore_index=1)
print(concaniate)