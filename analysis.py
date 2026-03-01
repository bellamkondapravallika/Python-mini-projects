import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("students.csv")
df["Total"]=df["Maths"]+df["Physics"]+df["English"]
df["Average"]=df["Total"]/3
print("Students Data:")
print(df)
top_student=df.loc[df["Total"].idxmax()]
print("\nTop scorer:")
print(top_student["Name"])
plt.bar(df["Name"],df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")
plt.show()