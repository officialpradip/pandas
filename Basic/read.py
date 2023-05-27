import pandas as pd

demo = pd.read_csv("./train.csv")
# print(demo)

# print(demo["PassengerId"])

print(demo.head(6))
print(demo.tail(3))
