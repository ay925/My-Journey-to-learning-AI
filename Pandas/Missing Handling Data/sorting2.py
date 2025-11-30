import pandas as pd
data={
    "Name":["Anupam","Anshu","Ayush"],
    "Age":[10,20,8],
    "Salary":[1000,29999,222222]

}
df=pd.DataFrame(data)
df.sort_values(by=["Age","Salary"],ascending=[True,True],inplace=True)
print(df)