import pandas as pd
data={"Name":["Anupam","Anshu","Aryan","Ayush","Abhinav"],
      "Age":[18,19,18,17,18],
      "City":["Jaunpur","Jaunpur","Varansi","Hardoi","Gonda"]
      }
df=pd.DataFrame(data)
# df.to_csv("Pandas/student_info.csv",index=False)
# df.to_excel("Pandas/student_info.xlsx",index=False)
df.to_json("Pandas/student_info.json",index=False)
print(df)
