import pandas as pd
df=pd.read_csv("Pandas/Project/studentdataclening/basic_students_csv_preview.csv")
df.dropna(subset=["math_score","english_score"],how="all")
df.fillna(df["math_score"].mean())
print(df)