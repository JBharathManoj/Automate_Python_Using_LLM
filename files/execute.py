import pandas as pd

df = pd.read_csv(r"input.csv")
filtered_data = df[df['Salary'] > 10000]
filtered_data.to_csv(r"output.txt", index=False)