import pandas as pd

# Customer Profile DataFrame
customer_data = {
    "CustomerID": ["C001","C002","C003","C004","C005"],
    "Name": ["Rohan Sharma","Priya Verma","Amit Singh","Neha Kapoor","Arjun Mehta"],
    "Age": [28, 32, 24, 29, 35],
    "City": ["Delhi","Mumbai","Bengaluru","Kolkata","Hyderabad"],
    "Email": ["rohan@example.com","priya@example.com","amit@example.com","neha@example.com","arjun@example.com"],
    "JoinDate": ["2023-01-15","2022-11-04","2023-03-10","2023-02-21","2021-12-18"]
}

customers_df = pd.DataFrame(customer_data)

# Transaction History DataFrame
transactions_data = {
    "TransactionID": ["T1001","T1002","T1003","T1004","T1005"],
    "CustomerID": ["C001","C003","C002","C005","C004"],
    "Date": ["2023-04-02","2023-04-05","2023-04-06","2023-04-07","2023-04-10"],
    "Amount": [1200, 850, 5400, 300, 2100],
    "PaymentMethod": ["UPI","Card","NetBanking","Cash","UPI"],
    "Status": ["Completed","Completed","Pending","Completed","Failed"]
}

transactions_df = pd.DataFrame(transactions_data)

merging=pd.merge(customers_df,transactions_df,on="CustomerID")
concaniate=pd.concat([customers_df,transactions_df],axis=1,ignore_index=1)
# print(merging)
# df=pd.DataFrame(concaniate)
df=pd.DataFrame(merging)
df.to_excel("Pandas/Merging&Joining/h.w/Customermerging.xlsx")
print("Succsessfully!!")