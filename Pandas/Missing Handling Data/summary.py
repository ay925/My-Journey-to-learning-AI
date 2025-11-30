import pandas as pd
data={
    "Name":["Anupam","Anshu","Ayush"],
    "Age":[10,20,8],
    "Salary":[1000,29999,222222]

}
df=pd.DataFrame(data)
avrage_salary=df["Salary"].mean()
print(avrage_salary)