import pandas as pd
demo = pd.read_csv("./train.csv")
print(demo.head(5))

# select specific colums
ages = demo[["Age", "Sex"]]
print(ages)
print(ages.shape)

# filter columns
thirty_fice = demo[demo["Age"] > 35]
print("thisis++++++", thirty_fice)
