import pandas as pd
# df=pd.read_json("Pandas/sample_Data.json")
data={"Name":["Anupam","Anshu","Aryan","Ayush","Abhinav"],
      "Age":[18,19,18,17,18],
      "City":["Jaunpur","Jaunpur","Varansi","Hardoi","Gonda"]
      }
df=pd.DataFrame(data)
print("Displaying the info of data set \n")
print(df.info())