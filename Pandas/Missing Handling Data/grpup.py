import pandas as pd
data={
    "Name":["Anupam","Anshu","Ayush","Abhinav","Aryan","Krishna","Chirnjiv","Aditya","Ansh"],
    "Age":[10,20,8,8,8,7,6,5,5],
    "Salary":[1000,29999,222222,1000,20000,200000,30000223,7878787878,76788778]
}
df=pd.DataFrame(data)
groped=df.groupby("Age")["Salary"].sum()
print(groped)

