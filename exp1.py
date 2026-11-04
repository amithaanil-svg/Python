import pandas as pd
data={
    'Name': ['ABHI', 'ASWIN', 'ANJALI', 'JOEL', 'JIBIN', 'APARNA'],
    'Age': [20, 23, 17, 16, 21, 25,],
    'Department': ['BCA', 'MCA', 'BTECH', 'MCA', 'BCA', 'HR'],
    'Salary': [50000,60000,6500,7000,50000,60000,],
}
df=pd.DataFrame(data)
print("orginal data frame:\n")
print(df)
print("\n first 3 rows)\n")
print(df.head(3))
print("\n data frame information:")
print(df.info())
print("\n statistical summary:")
print(df.describe())